import string
from typing import Tuple

import requests
import crawling_by_id
import analysis
import connect_mysql


def search_for_id_and_package_by_name(app_name: string):
    url = 'https://www.taptap.io/webapiv2/mix-search/v2/by-keyword'
    param_xua = 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    params = {
        'kw': app_name,
        'X-UA': param_xua
    }
    response = requests.get(url=url, params=params, headers=headers)
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


def crawling_by_app_name(app_name: string, app_package: string):
    app_info = search_for_id_and_package_by_name(app_name)
    if app_info is None:
        print('crawling failed')
        return
    elif app_info[1] != app_package:
        print('package validation failed')
        return
    else:
        return crawling_by_id.crawling_by_app_id(app_info[0], app_name)


def crawling_by_app_names_and_packages(apps: Tuple, db):
    for app in apps:
        texts = crawling_by_app_name(app[0], app[1])
        if texts is not None:
            for text in texts:
                tuples = analysis.analysis_game_comment_json_to_tuple(text, app[2])
                for value in tuples:
                    connect_mysql.insert_result_comment(db, value)
