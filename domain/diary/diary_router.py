from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db

from domain.user.user_router import get_current_user
from models import User
from domain.diary import diary_crud, diary_schema

router = APIRouter (
    prefix="/api/diary",
    tags = ["diary"]
)

@router.get("/list",response_model=list[diary_schema.Diary])
def diary_list(db: Session = Depends(get_db),
               current_user : User = Depends(get_current_user)):

    _diary_list = diary_crud.get_diary_list(db, current_user)

    return _diary_list

@router.get("/detail/{diary_id}",response_model=diary_schema.Diary)
def diary_detail(diary_id:int, db:Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):
    diary = diary_crud.get_diary(db, diary_id)

    if current_user.id != diary.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="권한이 없습니다."
        )

    return diary

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def diary_create(_diary_create : diary_schema.DiaryCreate,
                 db: Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):

    diary_crud.create_diary(db,_diary_create,current_user)

@router.put("/update")
def diary_update(_diary_update : diary_schema.DiaryUpdate,
                 db: Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):

    db_diary = diary_crud.get_diary(db,_diary_update.diary_id)

    if not db_diary :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을 수 없습니다."
        )

    if current_user.id != db_diary.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="수정 권한이 없습니다."
        )

    diary_schema.update_diary(db = db, db_diary = db_diary,
                              _diary_update = _diary_update)

@router.delete("/delete/{diary_id}")
def diary_delete(diary_id : int,
                 db: Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):

    db_diary = diary_crud.get_diary(db, diary_id= diary_id)

    if not db_diary :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을 수 없습니다."
        )

    if current_user.id != db_diary.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="삭제 권한이 없습니다."
        )

    diary_crud.delete_diary(db, diary_id= diary_id)