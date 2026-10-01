from fastapi import FastAPI
from routes.student_routes import router as student_router

app = FastAPI(
    title="Student CRUD API",
    description="A simple Student Management REST API using FastAPI",
    version="1.0.0"
)

app.include_router(student_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student CRUD API",
    }