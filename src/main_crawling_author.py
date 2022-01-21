import crawling_author_by_id
import connect_mysql

if __name__ == '__main__':
    ids = connect_mysql.select_author_id()
    db = connect_mysql.open_des_database()
    crawling_author_by_id.crawling_author_by_ids(author_ids=ids, is_print=True, db=db)
    connect_mysql.close_des_database(db)
