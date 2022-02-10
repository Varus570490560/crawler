import connect_mysql
import key_word_replace

if __name__ == '__main__':
    db = connect_mysql.open_des_database()
    key_word_replace.word_replace(db=db, before_key="\\n", after_key='\n')
