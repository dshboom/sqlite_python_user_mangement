import sqlite3
database_position = "./database/user.db"
class UserRepository:
    def __init__(self, database_position):
        self.database_position = database_position
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.database_position)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        print("数据库连接已关闭... ...")
        
    def register_user(self, user_name, hashed_password):
        try:
            user_info = (user_name , hashed_password)
            sql_command = "INSERT INTO user_table (user_name, hashed_password) VALUES (?, ?)"
            self.cursor.execute(sql_command, user_info)
            self.conn.commit()
            print("注册成功")
            return True
        except sqlite3.IntegrityError:
            print(f"注册失败，数据库错误：用户名 '{user_name}' 已存在。")
            return False
        except sqlite3.Error as e:
            print(f"注册失败，数据库错误{e}")
            return False
        
        
    def find_user_by_name(self, user_name):
        user_info = (user_name,)
        sql_command = "SELECT hashed_password FROM user_table WHERE user_name = ?"
        self.cursor.execute(sql_command)
        result = self.cursor.fetchone()
        return result[0] if result else None
        


        
