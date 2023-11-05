from sqlalchemy.orm import Session
from models import ImDiary, User
from datetime import datetime

from domain.imdiary.imdiary_schema import ImDiaryCreate, ImDiaryUpdate

def get_imdiary_list(db:Session,current_user):
    i_list = db.query(ImDiary)\
        .filter(ImDiary.user_id == current_user.id) \
        .order_by(ImDiary.create_date.desc()).all()

    return i_list

# 이미지 파일 전송하는 건 여기 데베 안거치고 router에서 바로 처리
# 객체 하나 받는건 생성X -> delete때문에 생성
def get_imdiary(db: Session, imdiary_id : int):
    imdiary = db.query(ImDiary).get(imdiary_id)
    return imdiary
def create_imdiary(db : Session, image_url : str, user : User):
    _imdiary = ImDiary(create_date = datetime.now(),
                       image = image_url,
                       user = user)

    db.add(_imdiary)
    db.commit()

def delete_imdiary(db:Session, imdiary_id : int):
    d_imdiary = db.query(ImDiary).get(imdiary_id)
    db.delete(d_imdiary)
    db.commit()