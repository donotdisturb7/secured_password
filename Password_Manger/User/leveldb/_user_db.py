import sqlite3
import os

def create_dbtable():
    conn = sqlite3.connect(r"Password_Manger/User/leveldb/user.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS UserDateBAse
                     (ID    INT     Primary     Key,
                    Username    CHAR(50),
                     Password    TEXT(100));''')
    conn.commit()
    conn.close()

def create_database():
    if os.path.exists("Password_Manger/User/leveldb/user.db"):
        create_dbtable()
        pass
    else:
        os.mkdir(r"Password_Manger/Users/leveldb")
        create_dbtable()

create_database()
