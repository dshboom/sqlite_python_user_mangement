import bcrypt
from user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def _password_hash(self, user_password):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def _verify_password(self, user_attmpt_password, sql_save_hashed_password):
        return bcrypt.checkpw(user_attmpt_password.encode('utf-8'), sql_save_hashed_password.encode('utf-8'))
    
    def register():
        pass
    
    def login():
        pass
    