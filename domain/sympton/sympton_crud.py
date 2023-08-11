from sqlalchemy.orm import Session
from models import Sympton,User
from datetime import datetime

from domain.sympton.sympton_schema import SymptonCreate

def create_sympton(db: Session, sympton_create : SymptonCreate,
                   user : User):

    _sympton = Sympton(create_date = datetime.now(),
                       user = user,
                       flushing_face = sympton_create.flushing_face,
                       sweating = sympton_create.sweating,
                       headache = sympton_create.headache,
                       dizziness = sympton_create.dizziness
                       )
    db.add(_sympton)
    db.commit()

def get_sympton_list(db: Session):
    s_list = db.query(Sympton).order_by(Sympton.create_date.desc()).all()

    return s_list
