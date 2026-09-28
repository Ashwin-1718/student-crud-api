from fastapi import HTTPException
from models.student_model import Student, StudentCreate

# In-memory storage (No Database)
students = {}
next_id = 1


# 1. Create Student
def create_student(student_data: StudentCreate):
    global next_id

    student = Student(
        id=next_id,
        **student_data.model_dump()
    )

    students[next_id] = student
    next_id += 1

    return student


# 2. Get All Students
def get_all_students():
    return list(students.values())


# 3. Get Student by ID
def get_student_by_id(student_id: int):
    student = students.get(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# 4. Update Student
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


# 5. Delete Student
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]