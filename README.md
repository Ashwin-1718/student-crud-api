# Student CRUD API

A simple Student Management REST API built using **FastAPI** and **Python**. This project provides CRUD (Create, Read, Update, Delete) operations for managing student records using in-memory storage.

## 🚀 Live Demo

**Swagger UI / API:**  
https://student-crud-api-8i49.onrender.com

> The root URL opens the interactive Swagger documentation directly.

### Main Endpoint

`/students/`

Supports:

- `POST /students/`
- `GET /students/`
- `GET /students/{student_id}`
- `PUT /students/{student_id}`
- `DELETE /students/{student_id}`

## ✨ Features

* Create a new student
* Retrieve all students
* Retrieve a student by ID
* Update existing student details
* Delete a student
* Input validation using Pydantic
* Proper HTTP status codes
* Interactive API documentation using Swagger UI

## 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

## 📁 Project Structure

```text
student-crud/
│
├── controllers/
│   └── student_controller.py
│
├── models/
│   └── student_model.py
│
├── routes/
│   └── student_routes.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Ashwin-1718/student-crud-api.git
```

### 2. Navigate to the project folder

```bash
cd student-crud-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

### 5. Open the API documentation

Visit:

http://127.0.0.1:8000/docs

## 🧪 Testing

Use Swagger UI to test all five CRUD endpoints.

1. Open `/docs`.
2. Select an endpoint.
3. Click **Try it out**.
4. Enter the required data.
5. Click **Execute** to view the response.

## 💾 Data Storage

This project uses in-memory storage. Student records are not permanently saved and are cleared whenever the application restarts.

## ☁️ Deployment

The application is deployed on Render using the GitHub repository.

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`

## 👨‍💻 Author

**Ashwin Yadav**

GitHub: [Ashwin-1718](https://github.com/Ashwin-1718)

Repository: [student-crud-api](https://github.com/Ashwin-1718/student-crud-api)
