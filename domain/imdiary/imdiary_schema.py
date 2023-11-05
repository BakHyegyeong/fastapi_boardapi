import datetime

from fastapi import UploadFile, File
from pydantic import BaseModel, validator

from domain.user.user_schema import User

class ImDiary(BaseModel):
    id : int
    create_date: datetime.datetime
    image : str
    user: User

    class Config :
        orm_mode = True

class ImDiaryList(BaseModel):
    diary_list : list[ImDiary] = []

class ImDiaryCreate(BaseModel):
    image : UploadFile

    @validator('image')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

class ImDiaryDelete(BaseModel):
    imdiary_id : int

class ImDiaryUpdate(ImDiaryCreate):
    imdiary_id: int