import sqlite3

conn = sqlite3.connect("./database/user.db")
cursor = conn.cursor()
sql_init_command = "CREATE TABLE user_table (id INTEGER PRIMARY KEY, user_name TEXT, hashed_password TEXT)"
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
