from sqlalchemy import Integer, Column, String
from database import Base

#Define the To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(50))
    