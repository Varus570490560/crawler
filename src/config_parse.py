import configparser
import os


class Url:
    def __init__(self, source):
        cf = configparser.ConfigParser()
        if source == 'com':
            cf.read('/Users/rockey211224/PycharmProjects/crawler/crawler/config/com_url.ini')
        elif source == 'io':
            cf.read('/Users/rockey211224/PycharmProjects/crawler/crawler/config/io_url.ini')
        else:
            print('config file parse error')
            exit(1)
        self.comment_url = cf.get('url', 'comment_url')
        self.search_url = cf.get('url', 'search_url')
        self.sub_comment_url = cf.get('url', 'sub_comment_url')
        self.author_url = cf.get('url', 'author_url')
