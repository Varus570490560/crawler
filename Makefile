craw_comment_com:
	python ./src/main_crawling_comment.py com
craw_comment_io:
	python3 ./src/main_crawling_comment.py io
craw_sub_comment_com:
	python ./src/main_crawling_sub_comment.py com
craw_sub_comment_io:
	python ./src/main_crawling_sub_comment.py io
craw_author_com:
	python ./src/main_crawling_author.py com
raw_author_io:
	python ./src/main_crawling_author.py io
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
