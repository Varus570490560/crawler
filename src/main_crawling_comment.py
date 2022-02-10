import sys
from time import sleep

import config_parse
import crawling_by_name
import connect_mysql
import muti_thread

if __name__ == '__main__':
    if len(sys.argv) == 1:
        source = 'com'
    else:
        source = sys.argv[1]
    url = config_parse.Url(source=source)
    apps = connect_mysql.select_app_name_package_id()
    app_lst = muti_thread.tuple_cut(apps, 1000)
    muti_thread.muti_thread_craw_comment(apps_lst=app_lst, is_print=False, search_url=url.search_url,
                                         comment_url=url.comment_url)
