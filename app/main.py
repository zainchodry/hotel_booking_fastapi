from fastapi import FastAPI
from app.database import *
from app.routes import bookings, users, rooms, hotels

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(bookings.router)
app.include_router(users.router)
app.include_router(rooms.router)
app.include_router(hotels.router)
