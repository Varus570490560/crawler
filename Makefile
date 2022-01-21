craw_comment:
	python ./src/main_crawling_comment.py
craw_sub_comment:
	python ./src/main_crawling_sub_comment.py
craw_author:
	python ./src/main_crawling_author.py
clear_comment_container:
	rm -f ./comment_container/*
clear_all_container:
	rm -f ./comment_container/* ./sub_comment_container/* ./author_container/*
clear_sub_comment_container:
	rm -f ./sub_comment_container/*
clear_author_container:
	rm -f ./author_container/*
test:
	python ./src/main_test.py
