import sys

import config_parse
import crawling_by_name
import connect_mysql

if __name__ == '__main__':
    url= config_parse.Url(source=sys.argv[1])
    apps = connect_mysql.select_app_name_package_id()
    db = connect_mysql.open_des_database()
    crawling_by_name.crawling_by_app_names_and_packages(apps, db, search_url=url.search_url, comment_url=url.comment_url)
    connect_mysql.close_des_database(db)
