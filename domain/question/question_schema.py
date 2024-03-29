import datetime

from pydantic import BaseModel, validator

from domain.answer.answer_schema import Answer
from domain.user.user_schema import User

class Question(BaseModel):
    id : int
    subject : str
    content : str
    tag : str
    create_date : datetime.datetime
    modify_date: datetime.datetime | None = None
    answers : list[Answer] = []
    user : User | None

    class Config :
        orm_mode = True

class QuestionList(BaseModel):
    total : int = 0
    question_list : list[Question] = []

class QuestionCreate(BaseModel):
    subject : str
    content : str
    tag : str

    @validator('subject','content','tag')
    def not_empty(cls, v):
        if not v or not v.strip() :
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class QuestionDelete(BaseModel):
    question_id : int

class QuestionUpdate(QuestionCreate):
    question_id : int
