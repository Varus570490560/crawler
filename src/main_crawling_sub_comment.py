import crawling_sub_comment
import connect_mysql

if __name__ == '__main__':
    ids_and_app_ids = connect_mysql.select_comment_id_app_id()
    db = connect_mysql.open_des_database()
    crawling_sub_comment.crawling_sub_comment_by_ids_and_app_ids(ids_and_app_ids=ids_and_app_ids, is_print=True, db=db)
    connect_mysql.close_des_database(db)
