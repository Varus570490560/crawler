import _thread
import threading
import crawling_by_name


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
        print("退出线程：" + str(self.name))


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
