# Ghee Ecommerce API Documentation

## Overview
This is a Django REST API for an e-commerce application with JWT authentication. Users can register, login, get profile info, reset passwords, and manage products with categories, variants, and images.

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
- **URL:** `POST http://127.0.0.1:8000/api/accounts/signup/`
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
- **URL:** `POST http://127.0.0.1:8000/api/accounts/login/`
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
- **URL:** `POST http://127.0.0.1:8000/api/accounts/token/refresh/`
- **Body (JSON):**
```json
{
    "refresh": "your_refresh_token_here"
}
```
- **Response:** Returns a new `access` token.

---

### 4. Get User Profile
- **URL:** `GET http://127.0.0.1:8000/api/accounts/profile/`
- **Headers:** 
  - Key: `Authorization`
  - Value: `Bearer your_access_token_here`
- **Response:** Returns user profile data (id, username, email, phone, address, role_name)

---

### 5. Password Reset
- **URL:** `POST http://127.0.0.1:8000/api/accounts/password_reset/`
- **Body (JSON):**
```json
{
    "email": "john@example.com"
}
```
- **Notes:** This triggers a password reset email (check console for the token in development).

---

## Product API Endpoints (Products Module)

All product endpoints start with: `http://127.0.0.1:8000/api/products/`

### 1. Categories
- **List all categories:** `GET /api/products/categories/`
- **Create category:** `POST /api/products/categories/` (Body: `{"name": "Category Name"}`)
- **Get single category:** `GET /api/products/categories/{id}/`
- **Update category:** `PUT /api/products/categories/{id}/`
- **Delete category:** `DELETE /api/products/categories/{id}/`

### 2. Units
- **List all units:** `GET /api/products/units/`
- **Create unit:** `POST /api/products/units/` (Body: `{"type": "weight", "value": "kg"}`)
- **Get single unit:** `GET /api/products/units/{id}/`
- **Update unit:** `PUT /api/products/units/{id}/`
- **Delete unit:** `DELETE /api/products/units/{id}/`

### 3. Products
- **List all products:** `GET /api/products/list/`
- **Create product:** `POST /api/products/list/`
```json
{
    "name": "Product Name",
    "description": "Product description",
    "category_id": 1
}
```
- **Get single product:** `GET /api/products/list/{id}/`
- **Update product:** `PUT /api/products/list/{id}/`
- **Delete product:** `DELETE /api/products/list/{id}/`

### 4. Product Variants
- **List all variants:** `GET /api/products/variants/`
- **Create variant:** `POST /api/products/variants/`
```json
{
    "product_id": 1,
    "price": "100.00",
    "quantity": 50,
    "size_value": "1",
    "unit_id": 1
}
```
- **Get single variant:** `GET /api/products/variants/{id}/`
- **Update variant:** `PUT /api/products/variants/{id}/`
- **Delete variant:** `DELETE /api/products/variants/{id}/`

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