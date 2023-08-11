from pydantic import BaseModel, validator
import datetime

from domain.user.user_schema import User

class Sympton(BaseModel):
    id : int
    create_date : datetime.datetime
    flushing_face: int
    sweating: int
    headache: int
    dizziness: int
    user : User

    class Config :
        orm_mode = True

class SymptonCreate(BaseModel):
    flushing_face : int
    sweating : int
    headache : int
    dizziness : int


