import traceback

from flask import jsonify

from services.user_service import UserService
from database.db_mysql import get_db
from models.base import generate_datetime
from utils.logger import Logger

from sqlalchemy.orm import Session
from models.user_model import UserModel as User
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"])
class AuthService():

    @classmethod
    async def login_user(cls, username: str, password:str, db: Session =next(get_db())):
        try:
            user = db.query(User).filter(User.username == username).first()
            if await AuthService.verify_password(password,user.password):
                user.last_login=generate_datetime()
                db.commit()
                db.refresh(user)
            else:
                print("Invalid credentials")

        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    async def register_user(cls, user : User):
        try:
            user['password']=AuthService.encrypt_password(user['password'])
            return  await UserService.create_user(user)
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def encrypt_password(cls,password):
        return password_context.hash(password)

    @classmethod
    async def verify_password(cls,password, hashed_pass):
     return password_context.verify(password, hashed_pass)