import datetime

from pydantic import BaseModel, validator

from domain.user.user_schema import User

class Diary(BaseModel):
    id : int
    subject : str
    content : str
    emotion : str
    create_date: datetime.datetime
    modify_date: datetime.datetime | None = None
    user: User

    class Config :
        orm_mode = True

class DiaryList(BaseModel):
    diary_list : list[Diary] = []

class DiaryCreate(BaseModel):
    subject : str
    content : str
    emotion : str

    @validator('subject', 'content', 'emotion')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class DiaryDelete(BaseModel):
    diary_id : int

class DiaryUpdate(DiaryCreate):
    diary_id : int