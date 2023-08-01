from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db:Session, user_create:UserCreate):
    db_user = User(username = user_create.username,
                   password=pwd_context.hash(user_create.password1),
                   email = user_create.email,
                   birthday = user_create.birthday)
    db.add(db_user)
    db.commit()

# 중복확인
def get_existing_user(db: Session, user_create : UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) |
        (User.email == user_create.email)
    ).first()

def get_user(db:Session, email: EmailStr):
    return db.query(User).filter(User.email == email).first()

