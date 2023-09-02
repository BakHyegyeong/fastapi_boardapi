from sqlalchemy.orm import Session
from models import Diary, User
from datetime import datetime

from domain.diary.diary_schema import DiaryCreate, DiaryUpdate

def get_diary_list(db: Session, current_user):
    d_list = db.query(Diary)\
        .filter(Diary.user_id == current_user.id)\
        .order_by(Diary.create_date.desc()).all()

    return d_list

def get_diary(db: Session, diary_id : int):
    diary = db.query(Diary).get(diary_id)
    return diary

def create_diary(db : Session,diary_create : DiaryCreate, user : User):
    _diary = Diary(subject = diary_create.subject,
                   content=diary_create.content,
                   emotion = diary_create.emotion,
                   create_date=datetime.now(),
                   user = user
                   )

    db.add(_diary)
    db.commit()

def delete_diary(db:Session, diary_id : int):
    d_diary = db.query(Diary).get(diary_id)
    db.delete(d_diary)
    db.commit()

def update_diary(db: Session, db_diary : Diary,
                 update_diary : DiaryUpdate):
    db_diary.subject = update_diary.subject
    db_diary.content = update_diary.content
    db_diary.emotion = update_diary.emotion
    db_diary.modify_date = datetime.now()

    db.add(db_diary)
    db.commit()

