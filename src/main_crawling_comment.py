import crawling_by_name
import connect_mysql

if __name__ == '__main__':
    apps = connect_mysql.select_app_name_package_id('localhost', 'root', '', 3306, 'jojoy')
    db = connect_mysql.open_des_database('localhost', 'root', '', 3306, 'game_comment')
    crawling_by_name.crawling_by_app_names_and_packages(apps, db)
    connect_mysql.close_des_database(db)
