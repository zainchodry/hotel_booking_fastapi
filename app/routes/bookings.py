from fastapi import APIRouter, HTTPException, Depends, status
from app.models import *
from app.database import *
from app.schemas.booking import *
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/bookings", response_model=BookingOut)
def create_booking(booking:BookingCreate, user_id:int, db:Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == booking.room_id).first()

    if not room:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Room Not Found")
    
    if not room.is_available:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Room Is Not Available")
    
    days = (booking.check_out - booking.check_in).days
    total_price = days * room.price

    new_booking = Booking(
        user_id=user_id,
        room_id=booking.room_id,
        check_in=booking.check_in,
        check_out=booking.check_out,
        total_price=total_price,
        status="confirmed"
    )
    room.is_available = False
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


@router.get("/booking/user/{user_id}", response_model=list[BookingOut])
def get_booking(user_id:int, db:Session = Depends(get_db)):
    bookings = db.query(Booking).filter(Booking.user_id == user_id).all()
    return bookings
