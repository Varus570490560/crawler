import string


import pymysql


def select_app_name_package(host: string, user: string, password: string, port: int, database: string):
    try:
        db = pymysql.connect(host=host, user=user, password=password, port=port, database=database)
        print('数据库连接成功')
    except pymysql.Error as e:
        print('数据库连接失败', e)
        return None
    cur=db.cursor()
    cur.execute("SELECT app.title,package.package_name FROM app INNER JOIN package WHERE app.id = package.app_id;")
    res = cur.fetchall()
    cur.close()
    db.close()
    return res



