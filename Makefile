craw_comment:
	python ./src/main_crawling_comment.py
craw_sub_comment:
	python ./src/main_crawling_sub_comment.py
clear_comment_container:
	rm -f ./comment_container/*
clear_all_container:
	rm -f ./comment_container/* ./sub_comment_container/*
clear_sub_comment_container:
	rm -f ./sub_comment_container/*
test:
	python ./src/main_test.py