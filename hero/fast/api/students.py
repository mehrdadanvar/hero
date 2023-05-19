from fastapi import FastAPI, APIRouter, Response
from pydantic import BaseModel
import hashlib
from db import database

router = APIRouter()


class Student(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str


class Loginstudent(BaseModel):
    email: str
    password: str


@router.get("/students")
async def get_students():
    return {"message": "working"}


@router.post("/students")
async def create_student(student: Student):
    print(student.firstname)
    student_collection = database["students"]
    h = hashlib.new("SHA256")
    h.update((student.password).encode())
    hashed_pass = h.hexdigest()
    print(hashed_pass)
    student_db_id = student_collection.insert_one(
        {"first_name": student.firstname, "last_name": student.lastname, "email": student.email, "password": hashed_pass})
    print(student_db_id)
    return {"student": [student.firstname, student.lastname, student.email, student.password, hashed_pass]}


@router.post("/studentlogin")
async def login_student(student: Loginstudent, response: Response):
    student_collection = database["students"]
    try:
        found_student = student_collection.find_one({"email": student.email})
        h = hashlib.new("SHA256")
        claimed_password = student.password
        h.update(claimed_password.encode())
        hashed_claimed_pass = h.hexdigest()
        found_password = found_student["password"]
        if hashed_claimed_pass == found_password:
            print("passwords match!")
            response.set_cookie(key="fakesession", value="somevalue")
            return {"status": "sucess", "data": [student.email, student.password]}
        else:
            print("password missmatch")
            return {"data": [student.email, student.password]}
    except:
        raise Exception("something went wrong")


def student_exists(student):
    student_collection = database["students"]
    try:
        found_student = student_collection.find_one({"email": student.email})
    except:
        print("failed")
