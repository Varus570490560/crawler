import sys
from time import sleep

import crawling_author_by_id
import connect_mysql
import config_parse

if __name__ == '__main__':
    url = config_parse.Url(source=sys.argv[1])
    ids = connect_mysql.select_author_id()
    db = connect_mysql.open_des_database()
    crawling_author_by_id.crawling_author_by_ids(author_ids=ids, is_print=False, db=db, author_url=url.author_url)
    while True:
        sleep(1)
    connect_mysql.close_des_database(db)
