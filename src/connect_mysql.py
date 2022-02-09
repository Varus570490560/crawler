import pymysql


def open_jojoy():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy', autocommit=True)
    except pymysql.Error as e:
        return None
    return db


def close_jojoy(db):
    db.close()


def select_app_name_package_id():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT distinct app.title,package_name,app.id FROM app WHERE `is_crawed`=0")
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
                'insert into `game_comment_1` (`id`,`created_time`,`star`,`device`,`author_id`,`like_count`,`dislike_count`,`reply_count`,`content`,`app_id`,`sub_comment`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,-1)',
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
        "SELECT id,app_id FROM game_comment_1 WHERE `sub_comment` = -1;")
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
        "select `author_id` FROM (select distinct author_id from game_comment_1 union select distinct `author_id` from `game_comment_2`)as a where author_id not in (select id as author_id from author) ;")
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


def select_icon_url_from_author():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment')
        print('源数据库连接成功')
    except pymysql.Error as e:
        print('源数据库连接失败', e)
        return None
    cur = db.cursor()
    cur.execute(
        "SELECT `name`,`icon_url` FROM `author`;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res


def update_game_comment_1_sub_comment_count(db, game_comment_1_id):
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'UPDATE `game_comment_1` SET `sub_comment`=1 WHERE `id` = %s;', game_comment_1_id)
            print(game_comment_1_id, " all sub comment deal successfully!!!")
        except pymysql.Error as err:
            print(err)


def update_app_set_is_crawed_1(db, app_id):
    with db.cursor() as cursor:
        try:
            cursor.execute(
                'UPDATE `app` SET `is_crawed`=1 WHERE `id` = %s;', app_id)
            print(app_id, " all comment deal successfully!!!")
        except pymysql.Error as err:
            print(err)
