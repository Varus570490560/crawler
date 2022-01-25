import sys

import crawling_sub_comment
import connect_mysql
import config_parse

if __name__ == '__main__':
    url = config_parse.Url(source=sys.argv[1])
    ids_and_app_ids = connect_mysql.select_comment_id_app_id()
    db = connect_mysql.open_des_database()
    crawling_sub_comment.crawling_sub_comment_by_ids_and_app_ids(ids_and_app_ids=ids_and_app_ids, is_print=False, db=db,
                                                                 sub_comment_url=url.sub_comment_url)
    connect_mysql.close_des_database(db)
