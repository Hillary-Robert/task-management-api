# Task Management API

A backend **Task Management API** built with **Django** and **Django REST Framework**.  
This project is part of my **Backend Capstone Project** and demonstrates core backend development skills such as authentication, permissions, CRUD operations, filtering, and deployment.

---

##  Features

- User registration, login, and logout using **Token Authentication**
- Create, Read, Update, and Delete (CRUD) tasks
- Mark tasks as **complete** or **incomplete**
- Prevent editing of completed tasks unless reverted to pending
- Task filtering by **status**, **priority**, and **due date**
- Task search by **title** or **description**
- Task ordering and pagination
- Object-level permissions (users can only access their own tasks)

---

## 🌍 Deployment

The API is deployed on **PythonAnywhere** and is publicly accessible.

**Base URL:**  

https://hillstech.pythonanywhere.com/


**API Root:**  
https://hillstech.pythonanywhere.com/api/



All task-related endpoints require authentication using a token.

---

## 🛠 Tech Stack

- Django
- Django REST Framework
- SQLite (development database)
- Postman (API testing)
- PythonAnywhere (deployment)

---

## ⚙️ Getting Started

### Clone the repository
```bash
git clone https://github.com/Hillary-Robert/task-management-api.git
cd task-management-api



## Install dependencies

pip install -r requirements.txt

## Run migrations
python manage.py migrate


## Start the development server


### Authentication

This API uses token-based authentication.

After logging in, include the token in request headers:

Authorization: Token <your_token>



API Endpoints
Authentication

POST /api/register/ – Register a new user

POST /api/login/ – Login and receive an authentication token

POST /api/logout/ – Logout and invalidate token

Tasks

GET /api/tasks/ – List all tasks for the authenticated user

POST /api/tasks/ – Create a new task

GET /api/tasks/<id>/ – Retrieve a specific task

PUT /api/tasks/<id>/ – Update a task

PATCH /api/tasks/<id>/ – Partially update a task

DELETE /api/tasks/<id>/ – Delete a task

POST /api/tasks/<id>/complete/ – Mark task as completed

POST /api/tasks/<id>/incomplete/ – Mark task as pending


Filtering
/api/tasks/?status=pending
/api/tasks/?priority=high

Search
/api/tasks/?search=meeting

Ordering
/api/tasks/?ordering=due_date
/api/tasks/?ordering=-created_at

Pagination
/api/tasks/?page=2



Permissions & Security

Only authenticated users can access the API

Users can only view and modify their own tasks

Object-level permissions enforced using a custom permission class

Completed tasks cannot be edited unless reverted to pending


Testing

All endpoints tested using Postman

Authentication flow verified

CRUD operations tested

Filtering, searching, ordering, and pagination confirmed

Permission restrictions validated