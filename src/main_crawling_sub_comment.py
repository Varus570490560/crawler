import crawling_sub_comment

if __name__ == '__main__':
    response_jsons = crawling_sub_comment.crawling_sub_commit_by_id(2147503881, 123, True)
    print(len(response_jsons))
