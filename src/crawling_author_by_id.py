import json
import threading
from time import sleep

import requests
import analysis
import connect_mysql
import time_out_exception


def crawling_author_by_id(author_id, is_print, author_url):
    response = None
    params = {
        'id': str(author_id),
        'X-UA': 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    cookies = {
        'locale': 'zh_CN',
        'tapadid': '29cadd85-c053-7264-9efb-c3e909d15856',
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d': 'eyJpdiI6IlRacXRiS3hTTHBZMjdlOUdNc0JNTnc9PSIsInZhbHVlIjoiekFXTFpYeEFua3FFN3ZsMm4rSStrV1NmeTRjSEV3ZnpFZ0g5cGNNeU1VVlNOSW1CQlwvdjhpZDZVM2VBY2c3WEFRVytiU2dzY1FOSXIrM29FaUNsZmdqbjJVdjdDbnhiR2RYRjRialU5M3FJPSIsIm1hYyI6IjBmZTBlZGE0OGM5YWY4ZGQxOWM2OTVhNTI5YWEyYzljZWVhZDhlMzJhNmMzMDBlYTkyNzgyYTVlYzYwMzU5NzIifQ%3D%3D',
        'user_id': '434091615',
        'ACCOUNT_LOGGED_USER_FROM_WWW': 'YT6S75wX0LGfwuqjIJRaBw%3D%3D',
        'CONSOLES_TOKEN_FROM_WWW': 'Qgre9KP9tv%2FJP6eM%2F77epA%3D%3D',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22434091615%22%2C%22%24device_id%22%3A%2217e719dc7f5519-0e2dead774e05e-1d326253-1296000-17e719dc7f6135e%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%2217e719dc7f5519-0e2dead774e05e-1d326253-1296000-17e719dc7f6135e%22%7D',
        '_gid': 'GA1.2.1065213382.1643078798',
        'apk_download_url_postfix': '/seo-baidu',
        '_gat': '1',
        '_ga_6G9NWP07QM': 'GS1.1.1643113479.19.1.1643114091.0',
        '_ga': 'GA1.1.1501180893.1642311321',
        'XSRF-TOKEN': 'eyJpdiI6IlJXZHNKT29SK1dLYk1xQnBBQmx2Q2c9PSIsInZhbHVlIjoiVmIxSjdBOFJEcWUxRHJqOUs2b2U5UVwvbUswNHNvSTNwWE5vYitZbkVqamdrdHZMbGhSUDN6cU9YVUtFemZqY1VVUERpK2FYUjJSck5vRDR3blpoWlVRPT0iLCJtYWMiOiI2NWI2MTdmZjYyZWM4OGJkNTUxNmY2YjNjMGUzYjc4Y2ExZDQ2MWQyZGZhNWQ3NDY4YWE2MWZhMTliZjc5ZjU1In0%3D',
        'tap_sess': 'eyJpdiI6IkVIVGJUbWlcL0dHT08yT29YRXpEV1wvQT09IiwidmFsdWUiOiI0R0dRamtpRHp3NTJcL2xUU1BQN0w3RFwvNllPa1RKbUNYcFBvK3NjU0Z0cXBDNk5nMzV6Y21GcDJmQm5OSFl0TlJcL2RMSEVKZWtMbkc3dXBkYjR4ZEVydz09IiwibWFjIjoiNGU1YzNjNjAzYTJkMWRlMWQ1ZmI3NzQzYTFiM2I1YWVjOTQ0MTU2MzdhMDNjYTcwZGRjY2FiZjA4NDA4YjZhNSJ9'
    }
    try:
        timer = threading.Timer(20, time_out_exception.throw_time_out_error)
        timer.start()
        response = requests.get(url=author_url, params=params, headers=headers, cookies=cookies)
        timer.cancel()
    except (time_out_exception.TimeOutError, requests.exceptions.SSLError) as e:
        print(e)
        print('There is a exception,Let me have a rest....')
        print('zzzZZ')
        sleep(5)
    if response is None:
        return None
    response_json = response.json()
    if is_print:
        file_name = './author_container/author author_id = ' + str(author_id) + '.json'
        with open(file_name, 'w', encoding='utf-8') as fp:
            json.dump(response_json, fp=fp, ensure_ascii=False, indent=4)
        print(file_name, "Saved!!!")
    return response_json


def crawling_author_by_ids(author_ids, is_print, author_url):
    db = connect_mysql.open_des_database()
    for author_id in author_ids:
        try:
            response_json = crawling_author_by_id(author_id[0], is_print, author_url=author_url)
            if response_json is None:
                continue
            response_tuple = analysis.analysis_author_json_to_tuple(response_json)
            connect_mysql.insert_author(db, response_tuple)
        except (KeyError, time_out_exception.TimeOutError) as e:
            print(e)
        finally:
            continue
