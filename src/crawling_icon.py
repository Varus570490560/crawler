import re
import threading
from time import sleep

import requests

from src import time_out_exception


def crawling_icon(author_infos):
    response = None
    if author_infos is None:
        return
    for author_info in author_infos:
        param_xua = 'V=1&PN=WebAppIntl&LANG=zh_TW&VN_CODE=59&VN=0.1.0&LOC=CN&PLT=PC&DS=Android&UID=22a3964e-db21-41a2-852d-f30283cda0f3&VID=434092598&DT=PC'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        analysis_url = re.split('/?', author_info[1])
        params = analysis_url[1]
        try:
            timer = threading.Timer(20, time_out_exception.throw_time_out_error)
            timer.start()
            response = requests.get(url=author_info[1], headers=headers)
            timer.cancel()
        except (time_out_exception.TimeOutError, requests.exceptions.SSLError) as e:
            print(e)
            print('There is a exception,Let me have a rest....')
            print('zzzZZ')
            sleep(5)
        if response is None:
            return None
        with open('../icon/' + author_info[0] + '.png', 'wb') as f:
            f.write(response.content)
        print(author_info[0], ' Saved !!!')
