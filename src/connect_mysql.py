import string

import pymysql


def select_app_name_package_id(host: string, user: string, password: string, port: int, database: string):
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, database=database)
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT app.title,package.package_name,app.id FROM app INNER JOIN package WHERE app.id = package.app_id;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


def open_des_database(host: string, user: string, password: string, port: int, database: string):
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, database=database,autocommit=True)
        print('目的数据库连接成功')
    except pymysql.Error as e:
        print('目的数据库连接失败', e)
        return
    cur = db.cursor()
    return db


def insert_result_comment(db, value):
    print(value)
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'insert into `game_comment` (`created_time`,`star`,`device`,`author_id`,`like_count`,`dislike_count`,`reply_count`,`content`,`app_id`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                value)
            print('database saved!')
        except Exception as err:
            print(err)


def close_des_database(db):
    db.close()
