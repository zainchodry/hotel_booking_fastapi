from fastapi import APIRouter, HTTPException, Depends, status
from app.models import *
from app.database import *
from app.schemas.booking import *
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/rooms", response_model=RoomOut)
def add_room(room:RoomCreate, db:Session = Depends(get_db)):
    new_room = Room(**room.dict())
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


@router.get("/rooms", response_model=list[RoomOut])
def get_room(db:Session = Depends(get_db)):
    room = db.query(Room).filter(Room.is_available == True).all()
    return room
