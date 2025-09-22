import sqlite3
database_position = "./database/user.db"
class UserManager:
    def __init__(self, database_position):
        self.conn = sqlite3.connect(database_position)
        self.cursor = self.conn.cursor()

    def register_user(self, user_name, user_password):
        sql_command = "INSERT INTO user_table (user_name, hashed_password) VALUES (?, ?)"
        pass
    
    def login_user(self, user_name, user_password):
        pass
    
    def password_hash(self, user_password):
        pass
