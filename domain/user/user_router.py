from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from starlette import status


from datetime import timedelta, datetime

from database import get_db
from models import User
from domain.user import user_crud, user_schema
from domain.user.user_crud import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
SECRET_KEY = 'bbe9c6600741c250ced821b3ab8faee3165acb19837a0576a2af776f52b772d7'
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")


router = APIRouter(
    prefix="/api/user",
    tags = ["user"]
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
def login_for_access_token(form_data : OAuth2PasswordRequestForm = Depends(),
                            #form_data : user_schema.UserLogin,
                           db : Session = Depends(get_db)):

    # user_loginid(ID)를 사용하여 사용자 모델의 객체 가져오기
    user = user_crud.get_user(db, form_data.username)

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
        "sub" : user.user_loginid,
        "exp" : datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # 현재시각부터 24분
    }
    
    # 위의 정보, 암호화시 생성되는 64자리 랜덤문자열, 토큰 생성시 사용하는 알고리즘
    access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token" : access_token,
        "token_type" : "bearer",
        "user_loginid" : user.user_loginid
    }

def get_current_user(token : str = Depends(oauth2_scheme)  , db: Session = Depends(get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_loginid: str = payload.get("sub")
        if user_loginid is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    else:
        user = user_crud.get_user(db, user_loginid)

        if user is None:
            raise credentials_exception
        return user


@router.get("/detail/{user_loginid}")
def user_detail(user_loginid : str, db: Session = Depends(get_db),
                current_user : User = Depends(get_current_user)):

    user = user_crud.get_user(db, user_loginid = user_loginid)

    if not user :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을수 없습니다.")

    if current_user.id != user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="수정 권한이 없습니다."
        )

    return user

@router.put("/update")
def user_update(_user_update : user_schema.UserUpdate,
                db : Session = Depends(get_db),
                current_user : User = Depends(get_current_user)):
    db_user = user_crud.get_user(db, user_loginid= _user_update.user_loginid)

    if not db_user :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을수 없습니다.")

    if current_user.id != db_user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="수정 권한이 없습니다."
        )

    user_crud.update_user(db = db, db_user= db_user,
                          update_user= _user_update)


@router.delete("/delete/{user_loginid}")
def question_delete(user_loginid: str,
                    db: Session = Depends(get_db),
                    current_user : User = Depends(get_current_user)):

    db_user = user_crud.get_user(db, user_loginid=user_loginid)

    if not db_user :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터를 찾을수 없습니다.")

    if current_user.id != db_user.id :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="삭제 권한이 없습니다."
        )

    user_crud.delete_user(db = db, user_id = db_user.id)
