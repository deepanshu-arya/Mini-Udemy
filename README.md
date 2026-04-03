# 🎓 Mini Udemy - Online Learning Platform

A full-stack **Online Learning Platform** where instructors can upload courses and students can watch videos, manage learning, and track progress.

---

## 🚀 Features

### 👨‍🏫 Instructor Features

* Upload courses
* Add course videos
* Manage course content

### 🎓 Student Features

* Register & Login
* Browse courses
* Watch course videos
* Personal dashboard

### ⚙️ System Features

* REST API using FastAPI
* Video streaming support
* SQLite database integration
* Frontend with React
* API communication using Axios

---

## 🧠 Tech Stack

### Backend:

* FastAPI (Python)
* SQLite (Database)
* SQLAlchemy (ORM)
* Uvicorn (Server)

### Frontend:

* React.js
* Axios (API calls)
* HTML, CSS, JavaScript

### Storage:

* Local storage (for videos)
* Can be extended to cloud (AWS S3, Cloudinary)

---

## 📁 Project Structure

```
mini-udemy/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── schemas.py
│   ├── users.db
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── Login.js
│   │   ├── Register.js
│   ├── package.json
│
└── README.md
```

---

## ⚙️ How It Works

1. User registers via frontend
2. Frontend sends request to FastAPI backend
3. Backend stores user in database
4. User logs in
5. Courses are fetched from backend
6. Videos are streamed on frontend

---

## 🖥️ Run Backend (FastAPI)

### Step 1: Go to backend folder

```
cd backend
```

### Step 2: Install dependencies

```
pip install fastapi uvicorn sqlalchemy
```

### Step 3: Run server

```
uvicorn main:app --reload
```

### Backend runs at:

```
http://127.0.0.1:8000
```

### API Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Run Frontend (React)

### Step 1: Go to frontend folder

```
cd frontend
```

### Step 2: Install dependencies

```
npm install
```

### Step 3: Start React app

```
npm start
```

### Frontend runs at:

```
http://localhost:3000
```

---

## 🔗 API Connection

Frontend connects to backend using Axios:

```
http://127.0.0.1:8000
```

Make sure backend is running before starting frontend.

---

## ⚠️ Common Errors & Fixes

### ❌ Axios Network Error

👉 Backend not running or CORS issue

### ✅ Fix:

* Start backend server
* Enable CORS in FastAPI

---

### ❌ UNIQUE constraint failed

👉 Same email registered twice

### ✅ Fix:

* Use different email
* OR delete database file

---

## 👨‍💻 Author

* Developed by: Deepanshu
* Tech Enthusiast | Python Developer | AI Builder

---

## ⭐ Support

If you like this project:

* Give it a ⭐ on GitHub
* Share with others

---

## 📌 Note

This is a beginner-to-intermediate level full-stack project built for learning and real-world practice.

---

🔥 Happy Coding!
