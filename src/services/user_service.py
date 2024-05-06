import traceback

from sqlalchemy.orm import Session
from database.db_mysql import get_db

from utils.logger import Logger
from models.user_model import UserModel as User

class UserService():

    @classmethod
    async def create_user(cls, user:User, db: Session =next(get_db())):
        try:
            username,fullname,password=user.values()

            db_user = User(
            username=username,
            fullname=fullname,
            password=password)

            db.add(db_user)
            db.commit()
            db.refresh(db_user)

            return user
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
