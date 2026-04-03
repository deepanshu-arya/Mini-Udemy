from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class CourseCreate(BaseModel):
    title: str
    description: str