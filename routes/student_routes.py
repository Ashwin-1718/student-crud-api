from fastapi import APIRouter, status
from models.student_model import Student, StudentCreate
from controllers import student_controller

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# 1. Create Student
@router.post(
    "/",
    response_model=Student,
    status_code=status.HTTP_201_CREATED
)
def create_student(student_data: StudentCreate):
    return student_controller.create_student(student_data)


# 2. Get All Students
@router.get(
    "/",
    response_model=list[Student],
    status_code=status.HTTP_200_OK
)
def get_all_students():
    return student_controller.get_all_students()


# 3. Get Student by ID
@router.get(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def get_student_by_id(student_id: int):
    return student_controller.get_student_by_id(student_id)


# 4. Update Student
@router.put(
    "/{student_id}",
    response_model=Student,
    status_code=status.HTTP_200_OK
)
def update_student(student_id: int, student_data: StudentCreate):
    return student_controller.update_student(student_id, student_data)


# 5. Delete Student
@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):
    student_controller.delete_student(student_id)
    return None