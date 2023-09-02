from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database import get_db

from domain.user.user_router import get_current_user
from models import User
from domain.physicalpain import physicalpain_schema, physicalpain_crud

router = APIRouter (
    prefix="/api/physicalpain",
    tags = ["physicalpain"]
)

@router.get("/list", response_model=list[physicalpain_schema.PhysicalPain])
def physicalpain_list(db: Session = Depends(get_db),
                      current_user : User = Depends(get_current_user)):

    _physicalpain_list = physicalpain_crud.get_physicalpain_list(db, current_user)

    return _physicalpain_list

@router.get("/detail/{physicalpain_id}", response_model=physicalpain_schema.PhysicalPain)
def physicalpain_detail(physicalpain_id : int, db: Session= Depends(get_db),
                        current_user : User = Depends(get_current_user)):
    physicalpain = physicalpain_crud.get_physicalpain(db, physicalpain_id)

    if current_user.id != physicalpain.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="권한이 없습니다."
        )

    return physicalpain

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def physicalpain_create(_physicalpain_create : physicalpain_schema.PhysicalPainCreate,
                        db : Session = Depends(get_db),
                        current_user : User = Depends(get_current_user)):
    physicalpain_crud.create_physicalpain(db,_physicalpain_create,current_user)

@router.delete("/delete/{physicalpain_id}")
def physicalpain_delete(physicalpain_id : int,
                        db : Session = Depends(get_db),
                        current_user : User = Depends(get_current_user)):

    db_physicalpain = physicalpain_crud.get_physicalpain(db, physicalpain_id)

    if not db_physicalpain :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을 수 없습니다."
        )

    if current_user.id != db_physicalpain.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="삭제 권한이 없습니다."
        )

    physicalpain_crud.delete_physicalpain(db, physicalpain_id)