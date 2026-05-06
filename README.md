# 🚀 FastAPI Todo Application (NeonDB + Cloud Run)

A production-ready Todo API built using FastAPI, PostgreSQL (NeonDB), SQLAlchemy, and deployed directly using GitHub → Google Cloud Run.

---

## 📌 Features

- JWT Authentication (Register & Login)
- User Management
- Todo CRUD Operations
- Role-based Access (Admin/User)
- PostgreSQL Database (NeonDB)
- Direct Cloud Deployment (GitHub → Cloud Run)

---

## 🏗️ Tech Stack

- Backend: FastAPI
- Database: PostgreSQL (NeonDB)
- ORM: SQLAlchemy
- Authentication: JWT (python-jose)
- Password Hashing: bcrypt
- Server: Uvicorn
- Deployment: Google Cloud Run (Source-based, no Docker)

---

## 📂 Project Structure

```
FastapiProject/
│── TodoApp/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── routers/
│   │   ├── auth.py
│   │   ├── todos.py
│   │   ├── admin.py
│   │   ├── users.py
│
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚙️ Environment Variables

Set the following environment variable:

DATABASE_URL=postgresql+psycopg2://<username>:<password>@<host>:<port>/<dbname>?sslmode=require

Example (NeonDB):
postgresql+psycopg2://user:password@ep-xyz.neon.tech/dbname?sslmode=require

---

## ▶️ Run Locally

1. Clone the repository

git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo

2. Install dependencies

pip install -r requirements.txt

3. Run the application

uvicorn TodoApp.main:app --reload

4. Open in browser

API: http://localhost:8000  
Swagger Docs: http://localhost:8000/docs  

---

## ☁️ Deploy to Google Cloud Run (Using GitHub)

1. Push your project to GitHub

2. Go to Google Cloud Console

3. Navigate to:
Cloud Run → Create Service

4. Select:
- Source Repository (GitHub)
- Connect your GitHub account
- Select your repository

5. Configure Build:
- Runtime: Python 3.11
- Entry point:  
  uvicorn TodoApp.main:app --host 0.0.0.0 --port 8080

6. Set Environment Variable:
- DATABASE_URL = your NeonDB connection string

7. Click Deploy

---

## 🔐 Authentication APIs

### Register User

POST /auth/

Request Body:
{
  "username": "satyasai",
  "email": "sai@gmail.com",
  "first_name": "satya",
  "last_name": "sai",
  "password": "satyasai123",
  "role": "admin"
}

---

### Login

POST /auth/token

Form Data:
username=satyasai  
password=satyasai123  

Response:
{
  "access_token": "your_token",
  "token_type": "bearer"
}

---

## 📝 Todo APIs

| Method | Endpoint   | Description       |
| ------ | ---------- | ----------------- |
| GET    | /          | Get all todos     |
| GET    | /todo/{id} | Get specific todo |
| POST   | /todo      | Create todo       |
| PUT    | /todo/{id} | Update todo       |
| DELETE | /todo/{id} | Delete todo       |

---

## 👑 Admin APIs

| Method | Endpoint         | Description     |
| ------ | ---------------- | --------------- |
| GET    | /admin/todo      | Get all todos   |
| DELETE | /admin/todo/{id} | Delete any todo |
 

---

## 👤 User APIs
| Method | Endpoint       | Description      |
| ------ | -------------- | ---------------- |
| GET    | /user          | Get user details |
| PUT    | /user/password | Change password  |


---

## 🔒 Security

- Passwords hashed using bcrypt
- JWT-based authentication
- Role-based authorization (admin/user)

---

## 🚨 Important Notes

- DATABASE_URL must be set or app will fail
- NeonDB requires sslmode=require
- Do not hardcode secrets in code
- Use environment variables in Cloud Run

---

## 📌 Future Improvements

- Pagination
- Refresh Tokens
- Email Verification
- CI/CD automation with GitHub Actions

---

## 👨‍💻 Author

Satya Sai

---

⭐ If you like this project, give it a star!
