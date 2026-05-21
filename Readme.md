# Linkly

A backend URL management and analytics platform built using FastAPI. Linkly allows authenticated users to create shortened URLs, customize aliases, manage links, and track engagement analytics with built-in security and rate limiting.

---

## Features

- User registration and login using JWT authentication
- Password hashing for secure credential storage
- URL shortening with unique short codes
- Custom aliases for links
- Expiring links support
- Redirect handling
- Click analytics tracking
- User-specific dashboard
- IP-based rate limiting
- Layered architecture (Routes → Services → Repositories → Database)

---

## Tech Stack

**Backend**
- FastAPI
- Python

**Database**
- SQLite
- SQLAlchemy ORM

**Authentication**
- JWT
- Passlib (bcrypt)

**Validation**
- Pydantic

---

## Project Structure

```text
Linkly/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   └── url.py
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── security.py
│   │   └── rate_limiter.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── url.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   └── url_repository.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── url.py
│   │
│   ├── services/
│   │   └── url_service.py
│   │
│   └── main.py
│
├── requirements.txt
├── README.md

Architecture

Client
   ↓
FastAPI Routes
   ↓
Authentication Layer
   ↓
Service Layer
   ↓
Repository Layer
   ↓
SQLite Database

API Endpoints
Authentication
Method	Endpoint	Description
POST	/auth/register	Register new user
POST	/auth/login	Login and generate JWT token
URL Management
Method	Endpoint	Description
POST	/shorten	Create shortened URL
GET	/my-links	View all user links
GET	/{short_code}	Redirect to original URL


Example Workflow
Create URL

Request:

{
    "original_url":"https://github.com",
    "custom_alias":"resume",
    "expires_at":"2026-08-01T10:00:00"
}

Response:

{
    "short_url":"http://localhost:8000/resume"
}
Dashboard Response
{
    "total_links":2,
    "links":[
        {
            "original_url":"https://youtube.com",
            "short_code":"LHW4V9",
            "click_count":3
        },
        {
            "original_url":"https://github.com",
            "short_code":"resume",
            "click_count":1
        }
    ]
}
Security Features
JWT based authentication
Password hashing using bcrypt
Protected endpoints
User-specific resources
IP-based rate limiting

Run Locally

Clone repository:

git clone <repository-url>

Install dependencies:

pip install -r requirements.txt

Run application:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000/docs