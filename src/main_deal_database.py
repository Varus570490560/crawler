import pymysql

if __name__ == '__main__':
    try:
        comment_db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='game_comment',
                                     autocommit=True)
        jojoy_db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='jojoy',
                                   autocommit=True)
    except pymysql.Error as e:
        print(e)
    comment_cur = comment_db.cursor()
    comment_cur.execute(
        "SELECT `app_id`,count(1) FROM `game_comment_1` GROUP By `app_id`;")
    counts = comment_cur.fetchall()
    jojoy_cur = jojoy_db.cursor()
    for count in counts:
        try:
            jojoy_cur.execute("UPDATE `app` SET `comment_count` = %s WHERE `id` = %s", (count[1], count[0]))
            print('数据库更新成功')
        except pymysql.Error as e:
            print(e)
