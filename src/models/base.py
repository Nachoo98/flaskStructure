from datetime import datetime
import pytz
from sqlalchemy import Column, DateTime, Integer
from database.db_mysql import Base

def generate_datetime():
    return str(datetime.now(pytz.timezone("America/Argentina/Buenos_Aires")))

class BaseModel(Base):
    __abstract__ = True
    id= Column(Integer, primary_key= True ,autoincrement=True)
    created_at = Column(DateTime, default=generate_datetime)
    updated_at = Column(DateTime, default=generate_datetime)