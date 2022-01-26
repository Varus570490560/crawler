import connect_mysql
import crawling_icon

if __name__ == '__main__':
    authors = connect_mysql.select_icon_url_from_author()
    crawling_icon.crawling_icon(authors)
