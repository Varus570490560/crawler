from time import sleep

import pymysql


def word_replace(db, before_key, after_key):
    datas = None
    cur = db.cursor()
    try:
        cur.execute(
            "SELECT `id`,`content` FROM `game_comment_2` WHERE `content` LIKE '%\\n%'")
        datas = cur.fetchall()
        print('Total ', len(datas), ' to deal!')
        sleep(1)
    except pymysql.Error as e:
        print(e)
    for data in datas:
        deal = string_proc(before_string=data[1], before_key=before_key, after_key=after_key)
        try:
            cur.execute("UPDATE `game_comment_1` SET `content` = %s WHERE `id` =  %s", (deal, data[0]))
            print(deal)
        except pymysql.Error as e:
            print(e)
    cur.close()


def string_proc(before_string, before_key, after_key):
    return before_string.replace(before_key, after_key)
