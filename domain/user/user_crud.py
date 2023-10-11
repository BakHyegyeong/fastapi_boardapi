from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate, UserUpdate
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db:Session, user_create:UserCreate):
    db_user = User(username = user_create.username,
                   user_loginid = user_create.user_loginid,
                   password=pwd_context.hash(user_create.password1),
                   birthday = user_create.birthday)
    db.add(db_user)
    db.commit()

def delete_user(db:Session, user_id : int):
    d_user = db.query(User).get(user_id)
    db.delete(d_user)
    db.commit()

def update_user(db:Session, db_user : User,
                update_user : UserUpdate):
    db_user.username = update_user.username
    db_user.password = update_user.password1
    db_user.birthday = update_user.birthday
    db.add(db_user)
    db.commit()

# 중복확인
def get_existing_user(db: Session, user_create : UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.user_loginid == user_create.user_loginid)
    ).first()

def get_user(db:Session, user_loginid: str):
    return db.query(User).filter(User.user_loginid == user_loginid).first()

