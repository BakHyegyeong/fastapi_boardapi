import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi import UploadFile, File
from fastapi.responses import FileResponse
import os
from sqlalchemy.orm import Session
from starlette import status

from database import get_db

from domain.user.user_router import get_current_user
from models import User
from domain.imdiary import imdiary_crud, imdiary_schema

router = APIRouter (
    prefix="/api/imdiary",
    tags = ["imdiary"]
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# IMG_DIR = ".\images"
# IMG_DIR = os.path.join(BASE_DIR,'images')
IMG_DIR = "C:\project_Board\\board_api\domain\imdiary\images\\"

@router.get("/list",response_model=list[imdiary_schema.ImDiary])
def imdiary_list(db:Session = Depends(get_db),
                 current_user : User = Depends(get_current_user)):
    _imdiary_list = imdiary_crud.get_imdiary_list(db,current_user)

    return _imdiary_list

@router.get("/images/{file_name}")
def get_image(file_name:str):
    return FileResponse(file_name)

@router.post("/create",status_code=status.HTTP_204_NO_CONTENT)
async def imdiary_create(image: UploadFile,
                         db : Session = Depends(get_db),
                         current_user : User = Depends(get_current_user)):

    content = await image.read()
    imagename = f"{str(uuid.uuid4())}.jpg"

    # IMG_DIR에 imagename파일을 생성
    with open(os.path.join(IMG_DIR, imagename), "wb+") as fp:
        fp.write(content)

    # 이미지 경로
    image_url = ''.join([IMG_DIR,imagename])

    imdiary_crud.create_imdiary(db,image_url,current_user)


@router.delete("/delete/{imdiary_id}")
def imdiary_delete(imdiary_id : int,
                   db:Session = Depends(get_db),
                   current_user : User = Depends(get_current_user)):

    db_imdiary = imdiary_crud.get_imdiary(db, imdiary_id)

    if not db_imdiary:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을 수 없습니다."
        )

    if current_user.id != db_imdiary.user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="삭제 권한이 없습니다."
        )

    imdiary_crud.delete_imdiary(db, imdiary_id)

