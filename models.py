from sqlalchemy import Column, Integer, String,\
    Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base



class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String(500), nullable=False)
    content = Column(Text,nullable=False)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer,ForeignKey("user.id"), nullable=True)
    user = relationship("User",backref="question_users")
    modify_date = Column(DateTime, nullable=True)
    tag = Column(String(500), nullable = True)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("user.id"),nullable=True)
    user = relationship("User",backref="answer_users")
    modify_date = Column(DateTime, nullable=True)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(500), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    email = Column(String(500), unique=True, nullable=False)
    birthday = Column(String(500),nullable=False)


class Sympton(Base) :
    __tablename__ = "sympton"

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, nullable=False)
    flushing_face = Column(Integer, nullable=False)
    sweating = Column(Integer, nullable=False)
    headache = Column(Integer, nullable = False)
    condition = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User",backref="sympton_users")


class Diary(Base):
    __tablename__ = "diary"

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, nullable=False)
    modify_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="diary_users")
    subject = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    emotion = Column(String(500), nullable=False)

class PhysicalPain(Base):
    __tablename__ = "physicalpain"

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", backref="physicalpain_users")
    shoulder = Column(Boolean,nullable=False)
    elbow = Column(Boolean,nullable=False)
    finger = Column(Boolean,nullable=False)
    waist = Column(Boolean,nullable=False)
    wrist = Column(Boolean,nullable=False)
    joint = Column(Boolean,nullable=False)
    knee = Column(Boolean,nullable=False)
    ankle = Column(Boolean,nullable=False)


