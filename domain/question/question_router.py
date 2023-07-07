from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from domain.question import question_crud, question_schema
from starlette import status

router = APIRouter(
    prefix="/api/question",
)


@router.get("/list", response_model=list[question_schema.Question])
def question_list(db: Session = Depends(get_db)):
    _question_list = question_crud.get_question_list(db)

    return _question_list


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    return question


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)


@router.put("/update")
def question_update(_question_update: question_schema.QuestionUpdate,
                    db:Session = Depends(get_db)):
    db_question = question_crud.get_question(db, question_id = _question_update.question_id)
    question_crud.update_question(db = db, db_question = db_question,
                                  update_question = _question_update)


@router.delete("/delete/{question_id}")
def question_delete(question_id: int,
                    db: Session = Depends(get_db)):
    question_crud.delete_question(db=db, question_id=question_id)
