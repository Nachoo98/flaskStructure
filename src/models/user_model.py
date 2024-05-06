from sqlalchemy import  Column, String,DateTime
from models.base import BaseModel

class UserModel(BaseModel):
    __tablename__ = "user"
    username = Column(String(100))
    fullname = Column(String(100))
    password = Column(String(100))
    last_login = Column(DateTime, default=None)


