from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class HotelBase(BaseModel):
    name: str
    location: str
    description: Optional[str]

class HotelCreate(HotelBase):
    pass

class HotelOut(HotelBase):
    id: int
    class Config:
        from_attributes = True

class RoomBase(BaseModel):
    room_number: str
    room_type: str
    price: float
    is_available: Optional[bool] = True

class RoomCreate(RoomBase):
    hotel_id: int

class RoomOut(RoomBase):
    id: int
    hotel: HotelOut
    class Config:
        from_attributes = True

class BookingBase(BaseModel):
    room_id: int
    check_in: datetime
    check_out: datetime

class BookingCreate(BookingBase):
    pass

class BookingOut(BookingBase):
    id: int
    total_price: float
    status: str
    room: RoomOut
    class Config:
        from_attributes = True
