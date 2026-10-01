from fastapi import HTTPException
from models.student_model import Student, StudentCreate

students = {}
next_id = 1


def create_student(student_data: StudentCreate):
    global next_id

    student = Student(
        id=next_id,
        **student_data.model_dump()
    )

    students[next_id] = student
    next_id += 1

    return student


def get_all_students():
    return list(students.values())


def get_student_by_id(student_id: int):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


def update_student(student_id: int, student_data: StudentCreate):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_student = Student(
        id=student_id,
        **student_data.model_dump()
    )

    students[student_id] = updated_student

    return updated_student


def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]