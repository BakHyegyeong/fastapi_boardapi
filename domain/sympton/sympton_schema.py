from pydantic import BaseModel
import datetime


from domain.user.user_schema import User

class Sympton(BaseModel):
    id : int
    create_date : datetime.datetime
    flushing_face: int
    sweating: int
    headache: int
    condition: int
    user : User

    class Config :
        orm_mode = True

class SymptonCreate(BaseModel):
    flushing_face : int
    sweating : int
    headache : int
    condition : int



