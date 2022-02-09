import sys
from time import sleep

import crawling_author_by_id
import connect_mysql
import config_parse
import muti_thread

if __name__ == '__main__':
    if len(sys.argv) == 1:
        source = 'com'
    else:
        source = sys.argv[1]
    url = config_parse.Url(source=source)
    ids = connect_mysql.select_author_id()
    id_lst = muti_thread.tuple_cut(ids, 10000)
    muti_thread.muti_thread_craw_author(author_lst=id_lst, is_print=False, author_url=url.author_url)
