import string
from typing import Tuple

import requests
import crawling_by_id
import analysis
import connect_mysql
import threading
import time_out_exception


def search_for_id_and_package_by_name(app_name: string, search_url):
    response = None
    param_xua = 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    params = {
        'kw': app_name,
        'X-UA': param_xua
    }
    try:
        timer = threading.Timer(5, time_out_exception.throw_time_out_error,
                                'requests get search timeout')
        timer.start()
        response = requests.get(url=search_url, params=params, headers=headers)
        timer.cancel()
    except TimeoutError as e:
        print(e)
    if response is None:
        return None
    page_text = response.json()
    if 'success' not in page_text:
        print('search ', app_name, ' result response dont have key success.')
        return None
    elif not page_text['success']:
        print('search ', app_name, ' failed.')
        return None
    else:
        if len(page_text['data']['list']) == 0:
            print('search ', app_name, ' results count = 0')
            return None
        else:
            if page_text['data']['list'][0]['type'] != 'app':
                print('search ', app_name, ' results type isnt app')
                return None
            else:
                app_package_name = page_text['data']['list'][0]['app']['identifier']
                app_id = page_text['data']['list'][0]['app']['id']
                return app_id, app_package_name


def crawling_by_app_name(app_name: string, comment_url, search_url, app_package: string, log, is_print):
    app_info = search_for_id_and_package_by_name(app_name, search_url=search_url)
    if app_info is None:
        print('crawling failed')
        log_buffer = 'key_word: ' + str(app_name) + 'search failed'
        log.write(log_buffer + "\n\n")
        return
    elif app_info[1] != app_package:
        print('package validation failed')
        print('need: ', app_package)
        print('found: ', app_info[1])
        log_buffer = 'app_name: ' + str(app_name) + "\n" + ' need: ' + str(app_package) + "\n" + ' found: ' + str(
            app_info[1]) + "\n\n"
        log.write(log_buffer)
        log.flush()
        return
    else:
        return crawling_by_id.crawling_by_app_id(app_id=app_info[0], app_name=app_name, comment_url=comment_url,
                                                 is_print=is_print)


def crawling_by_app_names_and_packages(apps: Tuple, db, comment_url, search_url, is_print):
    tuples = None
    package_validation_failed_log = open('./package_validation_failed/package_validation_failed_log.txt', 'w')
    for app in apps:
        texts = crawling_by_app_name(app_name=app[0], app_package=app[1], search_url=search_url,
                                     comment_url=comment_url, log=package_validation_failed_log, is_print=is_print)
        if texts is not None:
            for text in texts:
                try:
                    tuples = analysis.analysis_game_comment_json_to_tuple(text, app[2])
                except KeyError as e:
                    print(e)
                for value in tuples:
                    connect_mysql.insert_comment(db, value)
    package_validation_failed_log.close()
