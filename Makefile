craw_comment:
	python ./src/main_crawling_comment.py
clear_comment_container:
	rm ./comment_container/*
clear_all_container:
	rm ./comment_container/* ./sub_comment_container/*
clear_sub_comment_container:
	rm ./sub_comment_container/*