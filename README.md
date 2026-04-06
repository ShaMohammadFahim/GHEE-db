# Ghee Ecommerce API Documentation

## Overview
This is a Django REST API for an e-commerce application with JWT authentication. Users can register, login, get profile info, and reset passwords.

## Tech Stack
- Django 5.2
- Django REST Framework
- SimpleJWT (JWT Authentication)
- PostgreSQL Database

---

## How to Run

### 1. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Start the Server
```bash
python manage.py runserver
```
The server will start at: `http://127.0.0.1:8000`

---

## API Endpoints & Postman Testing

### 1. User Registration (Signup)
- **URL:** `POST http://127.0.0.1:8000/api/signup/`
- **Body (JSON):**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "role_name": "Customer"
}
```
- **Notes:** `role_name` is optional. Default is "Customer". Other roles: "Admin", "Seller"

---

### 2. User Login
- **URL:** `POST http://127.0.0.1:8000/api/login/`
- **Body (JSON):**
```json
{
    "username": "john_doe",
    "password": "securepassword123"
}
```
- **Response:** Returns `access` and `refresh` tokens.
- **Important:** Copy the `access` token for authenticated requests.

---

### 3. Refresh Token
- **URL:** `POST http://127.0.0.1:8000/api/token/refresh/`
- **Body (JSON):**
```json
{
    "refresh": "your_refresh_token_here"
}
```
- **Response:** Returns a new `access` token.

---

### 4. Get User Profile
- **URL:** `GET http://127.0.0.1:8000/api/profile/`
- **Headers:** 
  - Key: `Authorization`
  - Value: `Bearer your_access_token_here`
- **Response:** Returns user profile data (id, username, email, phone, address, role_name)

---

### 5. Password Reset
- **URL:** `POST http://127.0.0.1:8000/api/password_reset/`
- **Body (JSON):**
```json
{
    "email": "john@example.com"
}
```
- **Notes:** This triggers a password reset email (check console for the token in development).

---

## Postman Setup Steps

1. **Open Postman**
2. **For Login/Signup (no auth needed):**
   - Select POST method
   - Enter URL
   - Go to Body tab → select "raw" → choose "JSON"
   - Enter JSON data
   - Click "Send"

3. **For Profile (requires auth):**
   - After login, copy the `access` token from response
   - Go to Headers tab
   - Add Key: `Authorization`
   - Add Value: `Bearer your_access_token`
   - Send request

---

## Database Configuration
- Database: PostgreSQL
- Name: `GHEE-db`
- User: `postgres`
- Password: `1234`
- Host: `localhost`
- Port: `5432`

Make sure PostgreSQL is running and the database `GHEE-db` exists before running migrations.