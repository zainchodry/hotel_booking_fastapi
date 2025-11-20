from fastapi import APIRouter, HTTPException, status, Depends
from app.models import User
from app.schemas.users import UserCreate, UserOut, Token
from app.utils.jwt_handler import *
from sqlalchemy.orm import Session
from app.database import get_db


router = APIRouter()

@router.post("/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user or db_user.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Email Or Password"
        )
    
    token = access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email Already Exists"
        )
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
