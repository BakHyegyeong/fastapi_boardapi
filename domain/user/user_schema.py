from pydantic import BaseModel, validator, EmailStr


class UserCreate(BaseModel):
    username: str
    user_loginid: str
    password1: str
    password2: str
    birthday : str

    @validator('username','user_loginid', 'password1', 'password2','birthday')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v

class UserLogin(BaseModel):
    user_loginid : str
    password : str

class UserDelete(BaseModel):
    user_loginid : str

class UserUpdate(BaseModel):
    user_loginid : str
    username: str
    password1: str
    password2: str
    birthday: str

    @validator('username', 'password1', 'password2', 'birthday')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('password2')
    def passwords_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다')
        return v

class Token(BaseModel):
    access_token : str
    token_type : str
    user_loginid : str

class User(BaseModel):
    id : int
    user_loginid:str
    username : str

    class Config:
        orm_mode = True
