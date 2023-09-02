from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from domain.user.user_router import get_current_user
from models import User
from domain.sympton import sympton_schema,sympton_crud
from starlette import status


router = APIRouter(
    prefix="/api/sympton",
    tags = ["sympton"]
)


@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
def sympton_create(_sympton_create : sympton_schema.SymptonCreate,
                   db: Session = Depends(get_db),
                   current_user : User = Depends(get_current_user)):

    sympton_crud.create_sympton(db = db, sympton_create= _sympton_create,
                                user = current_user)


@router.get("/list",response_model=list[sympton_schema.Sympton])
def sympton_list(db: Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):

    _sympton_list = sympton_crud.get_sympton_list(db,current_user)

    return _sympton_list

