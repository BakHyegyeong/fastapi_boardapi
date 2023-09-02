import datetime

from pydantic import BaseModel, validator

from domain.user.user_schema import User

class PhysicalPain(BaseModel):
    id : int
    create_date: datetime.datetime
    user : User
    shoulder : bool
    elbow : bool
    finger : bool
    wrist : bool
    waist : bool
    joint : bool
    knee : bool
    ankle : bool

    class Config :
        orm_mode = True


class PhysicalPainList(BaseModel):
    physicalpain : list[PhysicalPain] = []

class PhysicalPainCreate(BaseModel):
    shoulder: bool
    elbow: bool
    finger: bool
    wrist: bool
    waist: bool
    joint: bool
    knee: bool
    ankle: bool

class PhysicalPainDelete(BaseModel):
    physicalpain_id : int

class PhysicalPainUpdate(PhysicalPainCreate):
    physicalpain_id : int
