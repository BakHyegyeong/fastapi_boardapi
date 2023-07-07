from sqlalchemy import Column, Integer, String,\
    Text
from database import Base



class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String(500), nullable=False)
    content = Column(Text,nullable=False)