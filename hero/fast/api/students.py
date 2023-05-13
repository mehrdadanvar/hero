from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import hashlib

router = APIRouter()


class Student(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str


@router.get("/students")
async def get_students():
    collection = db["students"]
    students = collection.find()
    return {"students": ["mehrdad", "John", "Lucy"]}


@router.post("/students")
async def create_student(student: Student):
    print(student.firstname)
    student_collection = db["students"]
    h = hashlib.new("SHA256")
    h.update((student.password).encode())
    hashed_pass = h.hexdigest()
    print(hashed_pass)
    student_db_id = student_collection.insert_one(
        {"first_name": student.firstname, "last_name": student.lastname, "email": student.email, "password": hashed_pass})
    print(student_db_id)
    return {"student": [student.firstname, student.lastname, student.email, student.password, hashed_pass]}
