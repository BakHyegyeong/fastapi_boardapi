from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status


from datetime import timedelta, datetime

from database import get_db
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = 'bbe9c6600741c250ced821b3ab8faee3165acb19837a0576a2af776f52b772d7'
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/user",
)


@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_existing_user(db, user_create=_user_create)

    if user :
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")

    user_crud.create_user(db = db, user_create= _user_create)

# response_model은 return의 형태를 지정하는 것. 헷갈리지 말기...ㅠ
@router.post("/login", response_model=user_schema.Token)
def login_for_access_token(form_data : user_schema.UserLogin,
                           db : Session = Depends(get_db)):

    # email(ID)를 사용하여 사용자 모델의 객체 가져오기
    user = user_crud.get_user(db, form_data.email)

    # 사용자 모델 객체가 아니거나 입력비밀번호와 저장된 비밀번호가 다를경우 오류발생
    # pwd_context의 verify함수는 암호화되지 않은 비밀번호(입력 비밀번호)를 암호화해서
    # 저장된 비밀번호와 일치하는지 판단!
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # jwt(json web token)을 사용하여 액세스 토큰 생성
    # 사용자 ID와 토큰의 유효기간 설정.
    data = {
        "sub" : user.email,
        "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # 현재시각부터 24분
    }
    
    # 위의 정보, 암호화시 생성되는 64자리 랜덤문자열, 토큰 생성시 사용하는 알고리즘
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token" : access_token,
        "token_type" : "bearer",
        "email" : user.email
    }






