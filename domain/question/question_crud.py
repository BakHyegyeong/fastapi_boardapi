from sqlalchemy.orm import Session
from models import Question
from domain.question.question_schema import QuestionCreate,QuestionUpdate


def get_question_list(db: Session):
    q_list = db.query(Question).all()

    return q_list

def get_question(db: Session, question_id: int):
    question = db.query(Question).get(question_id)
    return question


def create_question(db: Session, question_create: QuestionCreate):
    _question = Question(subject=question_create.subject,
                         content=question_create.content)
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
    db.add(db_question)
    db.commit()


