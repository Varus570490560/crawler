import crawling_by_name
import connect_mysql

if __name__ == '__main__':
    apps = connect_mysql.select_app_name_package('localhost', 'root', '', 3306, 'jojoy')
    crawling_by_name.crawling_by_app_names_and_packages(apps)
