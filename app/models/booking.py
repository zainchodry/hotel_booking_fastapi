from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String)

    rooms = relationship("Room", back_populates="hotel")


class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(String, nullable=False)
    room_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room")


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="pending")

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")
