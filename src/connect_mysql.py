import pymysql


def select_app_name_package_id():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT distinct app.title,package.package_name,app.id FROM app INNER JOIN package WHERE app.id = package.app_id;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


def open_des_database():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment',
                             autocommit=True)
        print('目的数据库连接成功')
    except pymysql.Error as e:
        print('目的数据库连接失败', e)
        return
    return db


def insert_comment(db, value):
    print(value)
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'insert into `game_comment_1` (`id`,`created_time`,`star`,`device`,`author_id`,`like_count`,`dislike_count`,`reply_count`,`content`,`app_id`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                value)
            print('database saved!')
        except pymysql.Error as err:
            print(err)


def close_des_database(db):
    db.close()


def select_comment_id_app_id():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT id,app_id FROM game_comment_1;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


def insert_sub_comment(db, value):
    print(value)
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'insert into `game_comment_2` (`id`,`app_id`,`main_comment_id`,`created_time`,`author_id`,`to_author_id`,`content`,`like_count`) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                value)
            print('database saved!')
        except pymysql.Error as err:
            print(err)


def select_author_id():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT distinct author_id FROM game_comment_1 UNION select distinct author_id FROM game_comment_2;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


def insert_author(db, value):
    print(value)
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'insert into `author` (`id`,`name`,`following_count`,`fans_count`,`introduction`,`icon_url`) values(%s,%s,%s,%s,%s,%s)',
                value)
            print('database saved!')
        except pymysql.Error as err:
            print(err)


def select_app_id_from_game_comment_1():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT distinct app_id FROM game_comment_1;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res

