from fastapi import FastAPI, APIRouter, Response
from pydantic import BaseModel
import hashlib
from db import database

router = APIRouter()


class Student(BaseModel):
    firstname: str
    lastname: str
    email: str


@router.get("/coordinators")
async def read_students():
    student_collection = database["students"]
    raw_students = student_collection.find({})
    cleaned_students = []
    for student in raw_students:
        print(student)
        print(type(student))
        cleaned_students.append({"firstname": student["first_name"]})
    return {"students": cleaned_students}
