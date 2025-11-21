
# Hotel Booking FastAPI Project

## Overview
This is a complete **Hotel Booking System** built using **FastAPI**, **SQLAlchemy**, and **Pydantic**.  
It supports:
- User authentication (signup & login)
- Hotels management
- Rooms management
- Room booking system
- Price calculation
- Database persistence using SQLAlchemy ORM
- Auto-generated Swagger API documentation

---

## Features

### ✅ **User Authentication**
- User signup
- User login
- Password hashing using `passlib`

---

### ✅ **Hotels Management**
- Create hotels
- List all hotels

---

### ✅ **Rooms Management**
- Create rooms
- List all rooms
- Assign rooms to hotels

---

### ✅ **Bookings**
- Create room bookings
- Auto calculate price based on number of days
- Fetch user bookings

---

## Project Structure

```
hotel_booking_fastapi/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── hotels.py
│   │   ├── rooms.py
│   │   └── bookings.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/zainchodry/hotel_booking_fastapi.git
cd hotel_booking_fastapi
```

---

## Install Dependencies
You must install all packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open your browser at:

```
http://127.0.0.1:8000/docs
```

You will see fully interactive **Swagger API documentation**.

---

## API Endpoints Overview

### 🔐 **Authentication**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/signup` | Create a new user |
| POST | `/auth/login` | Login user |

---

### 🏨 **Hotels**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/hotels/` | Create hotel |
| GET | `/hotels/` | List hotels |

---

### 🚪 **Rooms**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/rooms/` | Create room |
| GET | `/rooms/` | List rooms |

---

### 📅 **Bookings**
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/bookings/?user_id=1` | Create booking |
| GET | `/bookings/user/{user_id}` | Get user bookings |

---

## Database
The project uses:

```
SQLite (default)
```

You can switch to PostgreSQL by editing:

```
DATABASE_URL in database.py
```

---

## License
This project is free to use for learning and development.

---

## Author
**Zain - (enigmatix)**  
Full-stack Python & Django Developer

---
