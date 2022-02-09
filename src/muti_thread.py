import threading
import crawling_by_name
import crawling_sub_comment
import crawling_author_by_id


class CrawlingCommentThread(threading.Thread):
    def __init__(self, thread_id, input_datas, is_print, comment_url, search_url):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.input_datas = input_datas
        self.is_print = is_print
        self.comment_url = comment_url
        self.search_url = search_url

    def run(self):
        print("开始线程：" + str(self.thread_id))
        crawling_by_name.crawling_by_app_names_and_packages(apps=self.input_datas, is_print=self.is_print,
                                                            search_url=self.search_url, comment_url=self.comment_url)
        print("退出线程：" + str(self.thread_id))


class CrawlingSubCommentThread(threading.Thread):
    def __init__(self, thread_id, input_datas, is_print, sub_comment_url):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.input_datas = input_datas
        self.is_print = is_print
        self.sub_comment_url = sub_comment_url

    def run(self):
        print("开始线程：" + str(self.thread_id))
        crawling_sub_comment.crawling_sub_comment_by_ids_and_app_ids(ids_and_app_ids=self.input_datas,
                                                                     is_print=self.is_print,
                                                                     sub_comment_url=self.sub_comment_url)
        print("退出线程：" + str(self.thread_id))


class CrawlingAuthorThread(threading.Thread):
    def __init__(self, thread_id, input_datas, is_print, author_url):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.input_datas = input_datas
        self.is_print = is_print
        self.author_url = author_url

    def run(self):
        print("开始线程：" + str(self.thread_id))
        crawling_author_by_id.crawling_author_by_ids(author_ids=self.input_datas, is_print=self.is_print,
                                                     author_url=self.author_url)
        print("退出线程：" + str(self.thread_id))


def tuple_cut(main_tuple, sub_tuple_len):
    lst = []
    for i in range(0, len(main_tuple), sub_tuple_len):
        lst.append((main_tuple[i:i + sub_tuple_len]))
    return lst


def muti_thread_craw_comment(apps_lst, is_print, search_url, comment_url):
    i = 0
    for apps in apps_lst:
        i = i + 1
        CrawlingCommentThread(thread_id=i, input_datas=apps, is_print=is_print, comment_url=comment_url,
                              search_url=search_url).start()


def muti_thread_craw_sub_comment(apps_lst, is_print, sub_comment_url):
    i = 0
    for apps in apps_lst:
        i = i + 1
        CrawlingSubCommentThread(thread_id=i, input_datas=apps, is_print=is_print,
                                 sub_comment_url=sub_comment_url).start()


def muti_thread_craw_author(author_lst, is_print, author_url):
    i = 0
    for author in author_lst:
        i = i + 1
        CrawlingAuthorThread(thread_id=i, input_datas=author, is_print=is_print,
                             author_url=author_url).start()
