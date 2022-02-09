import sys

import crawling_sub_comment
import connect_mysql
import config_parse
import muti_thread

if __name__ == '__main__':
    if len(sys.argv) == 1:
        source = 'com'
    else:
        source = sys.argv[1]
    url = config_parse.Url(source=source)
    ids_and_app_ids = connect_mysql.select_comment_id_app_id()
    datas = muti_thread.tuple_cut(main_tuple=ids_and_app_ids, sub_tuple_len=10000)
    muti_thread.muti_thread_craw_sub_comment(apps_lst=datas, is_print=False, sub_comment_url=url.sub_comment_url)
