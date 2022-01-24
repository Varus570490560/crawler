from typing import Any

import requests
import json
import os


def crawling_by_app_id_auto_increment(app_id_begin: int, app_id_end: int, app_name=""):
    if app_name != "":
        app_name = " " + app_name
    url = 'https://www.taptap.io/webapiv2/review/v2/by-app'
    param_app_id = app_id_begin
    param_limit = 10
    param_from = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    page_texts = list()
    while True:
        param = {
            'sort': 'hot',
            'app_id': str(param_app_id),
            'limit': str(param_limit),
            'from': str(param_from),
            'X-UA': 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
        }
        response = requests.get(url=url, params=param, headers=headers)
        page_text = response.json()
        page_texts.append(page_text)
        file_name = './comment_container/comment' + app_name + ' appID=' + str(param_app_id) + ' from=' + str(
            param_from) + '.json'
        with open(file_name, 'w', encoding='utf-8') as fp:
            json.dump(page_text, fp=fp, ensure_ascii=False, indent=4)
        print(file_name, "Saved!!!")
        if 'data' not in page_text:
            param_app_id += 1
            param_from = 0
        elif bool(1 - page_text['success']) or ('list' in page_text['data'] and len(page_text['data']['list'])) == 0:
            param_app_id += 1
            param_from = 0
        elif 'list' not in page_text['data']:
            param_app_id += 1
            param_from = 0
        else:
            param_from += 10
        if param_app_id == app_id_end + 1:
            break
    os.remove(file_name)
    return page_texts


def crawling_by_app_id(app_id: int, comment_url, is_print, app_name=""):
    if app_name != "":
        app_name = " " + app_name
    param_app_id = app_id
    param_limit = 10
    param_from = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response_jsons = list()
    while True:
        param = {
            'sort': 'hot',
            'app_id': str(param_app_id),
            'limit': str(param_limit),
            'from': str(param_from),
            'X-UA': 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
        }
        response = requests.get(url=comment_url, params=param, headers=headers)
        response_json = response.json()
        response_jsons.append(response_json)
        if len(response_json['data']['list']) != 0:
            response_jsons.append(response_json)
        if is_print:
            file_name = './comment_container/comment app_name = ' + app_name + ' from = ' + str(
                param_from) + '.json'
            with open(file_name, 'w', encoding='utf-8') as fp:
                json.dump(response_json, fp=fp, ensure_ascii=False, indent=4)
            print(file_name, "Saved!!!")
            if len(response_json['data']['list']) == 0:
                os.remove(file_name)
        if len(response_json['data']['list']) == 0:
            return response_jsons
        else:
            param_from += 10
