from fastapi import APIRouter, HTTPException, Depends, status
from app.models import *
from app.database import *
from app.schemas.booking import *
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/hotels", response_model=HotelOut)
def create_hotel(hotel:HotelCreate, db:Session = Depends(get_db)):
    new_hotel = Hotel(**hotel.dict())
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel

@router.get("/hotels", response_model=list[HotelOut])
def get_hotel(db:Session=Depends(get_db)):
    new_hotel = db.query(Hotel).all()
    return new_hotel
