from sqlalchemy.orm import Session
from models import Question, User
from datetime import datetime

from domain.question.question_schema import QuestionCreate,QuestionUpdate


def get_question_list(db: Session, skip: int = 0, limit: int = 5):
    _q_list = db.query(Question)\
        .order_by(Question.create_date.desc())

    total = _q_list.count()
    q_list = _q_list.offset(skip).limit(limit).all()

    return total, q_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question


def create_question(db: Session, question_create: QuestionCreate
                    ,user: User):
    _question = Question(subject=question_create.subject,
                         content=question_create.content,
                         create_date=datetime.now(),
                         user=user)
    db.add(_question)
    db.commit()

def delete_question(db: Session, question_id : int):
    d_question = db.query(Question).get(question_id)
    db.delete(d_question)
    db.commit()

def update_question(db: Session, db_question : Question,
                    update_question : QuestionUpdate):
    db_question.subject = update_question.subject
    db_question.content = update_question.content
    db_question.modify_date = datetime.now()
    db.add(db_question)
    db.commit()


