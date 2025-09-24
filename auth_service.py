import bcrypt
from user_repository import UserRepository

class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
    
    def _hash_password(self, user_password):
        salt = bcrypt.gensalt(rounds=12)
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def _verify_password(self, user_attempt_password, stored_hashed_password):
        return bcrypt.checkpw(user_attempt_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))
    
    def register(self, user_name, user_password):
        if self.user_repository.find_user_by_username(user_name):
            return False, "This name already exist!"
        else:
            hashed_password = self._hash_password(user_password)
            if self.user_repository.register_user(user_name, hashed_password):
                print("认证服务层：注册成功！")
                return True, "Register successfully!"
            else:
                print("认证服务层：注册失败！")
                return False, "Register failed!"
            
    def login(self, user_name, user_attempt_password):
        sql_save_user_password = self.user_repository.find_user_by_username(user_name)
        if sql_save_user_password:
            if self._verify_password(user_attempt_password,sql_save_user_password):
                print("认证服务层：登录成功！")
                return True, "Login successfully"
            else:
                print("认证服务层：用户名或密码错误！")
                return False, "User's name or password error!"
        else:
            print("认证服务层：用户名或密码错误！")
            return False, "User's name or password error!"