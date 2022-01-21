import json

import requests
import analysis
import connect_mysql


def crawling_author_by_id(author_id, is_print):
    url = 'https://www.taptap.io/webapiv2/user/v1/detail'
    params = {
        'id': str(author_id),
        'X-UA': 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    response = requests.get(url=url, params=params, headers=headers)
    response_json = response.json()
    if is_print:
        file_name = './author_container/author author_id = ' + str(author_id) + '.json'
        with open(file_name, 'w', encoding='utf-8') as fp:
            json.dump(response_json, fp=fp, ensure_ascii=False, indent=4)
        print(file_name, "Saved!!!")
    return response_json


def crawling_author_by_ids(author_ids, is_print, db):
    for author_id in author_ids:
        response_json = crawling_author_by_id(author_id[0], is_print)
        response_tuple = analysis.analysis_author_json_to_tuple(response_json)
        connect_mysql.insert_author(db, response_tuple)
