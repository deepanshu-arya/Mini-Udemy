from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models, schemas
from fastapi.middleware.cors import CORSMiddleware
import os
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    return {"message": "User registered"}

@app.post("/create-course")
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    return {"message": "Course created"}

@app.get("/courses")
def get_courses(db: Session = Depends(get_db)):
    return db.query(models.Course).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
