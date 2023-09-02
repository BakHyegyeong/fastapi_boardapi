from sqlalchemy.orm import Session
from models import PhysicalPain, User
from datetime import datetime

from domain.physicalpain.physicalpain_schema import PhysicalPainCreate, PhysicalPainUpdate


def get_physicalpain_list(db : Session, current_user):
    physicalpain_list = db.query(PhysicalPain)\
            .filter(PhysicalPain.user_id == current_user.id)\
            .order_by(PhysicalPain.create_date.desc()).all()

    return physicalpain_list


def get_physicalpain(db: Session, physicalpain_id : int):
    physicalpain = db.query(PhysicalPain).get(physicalpain_id)
    return physicalpain

def create_physicalpain(db: Session, physicalpain_create : PhysicalPainCreate,
                        user : User):
    _physicalpain = PhysicalPain(create_date=datetime.now(),
                                 user = user,
                                 shoulder = physicalpain_create.shoulder,
                                elbow  = physicalpain_create.elbow,
                                finger = physicalpain_create.finger,
                                wrist  = physicalpain_create.wrist,
                                waist  = physicalpain_create.waist,
                                joint = physicalpain_create.joint,
                                knee = physicalpain_create.knee,
                                ankle = physicalpain_create.ankle)

    db.add(_physicalpain)
    db.commit()

def delete_physicalpain(db: Session, physicalpain_id : int):
    d_physicalpain = db.query(PhysicalPain).get(physicalpain_id)
    db.delete(d_physicalpain)
    db.commit()

