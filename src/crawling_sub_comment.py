import json
import os

import requests
import analysis
import connect_mysql


def crawling_sub_comment_by_id(comment_id, is_print):
    url = 'https://www.taptap.io/webapiv2/review-comment/v1/by-review'
    param_from = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response_jsons = list()
    while True:
        params = {
            'review_id': str(comment_id),
            'order': 'asc',
            'show_top': '1',
            'limit': '10',
            'from': str(param_from),
            'X-UA': 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
        }
        response = requests.get(url=url, headers=headers, params=params)
        response_json = response.json()
        if len(response_json['data']['list']) != 0:
            response_jsons.append(response_json)
        if is_print:
            file_name = './sub_comment_container/sub_comment parent_comment_id = ' + str(comment_id) + ' from = ' + str(
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


def crawling_sub_comment_by_ids_and_app_ids(ids_and_app_ids, is_print, db):
    for id_and_app_id in ids_and_app_ids:
        response_jsons = crawling_sub_comment_by_id(id_and_app_id[0], is_print)
        for response_json in response_jsons:
            analysis_tuples = analysis.analysis_game_sub_comment_json_to_tuple(response_json, id_and_app_id)
            for analysis_tuple in analysis_tuples:
                connect_mysql.insert_sub_comment(db, analysis_tuple)
                print(analysis_tuple)