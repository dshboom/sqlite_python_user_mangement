import sqlite3
import os

database_position = "./database/user.db"
if not os.path.exists(database_position):
    print("数据库已存在，请删除 user.db 后再试!")
    exit()

conn = sqlite3.connect(database_position)
cursor = conn.cursor()
sql_init_command = "CREATE TABLE user_table (id INTEGER PRIMARY KEY, user_name TEXT NOT NULL UNIQUE, hashed_password TEXT NOT NULL UNIQUE)"
cursor.execute(sql_init_command)
conn.commit()
conn.close()
print("*****************初始化成功!*****************")
conn = sqlite3.connect("./database/user.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(user_table);")
conn.commit()
test_table = cursor.fetchall()
print("*****************表结构*****************")
print(test_table)
