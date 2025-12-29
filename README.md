# Task Management API

A backend Task Management system built with Django and Django REST Framework.
This project is part of my Backend Capstone Project.

## Features
- User registration, login, and logout (Token Authentication)
- Create, Read, Update, and Delete tasks
- Mark tasks as complete or incomplete
- Prevent editing completed tasks unless reverted
- Task filtering by status, priority, and due date
- Task search by title or description
- Task ordering and pagination
- Only the task owner can access their tasks

## Tech Stack
- Django
- Django REST Framework
- SQLite (Development)
- Postman (API Testing)

## Getting Started

```bash
git clone https://github.com/Hillary-Robert/task-management-api.git
cd task-management-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Authentication

This API uses token-based authentication.

Include the token in request headers:

Authorization: Token <your_token>

API Endpoints
Authentication

POST /api/register/

POST /api/login/

POST /api/logout/

Tasks

GET /api/tasks/ – list user’s tasks

POST /api/tasks/ – create a task

GET /api/tasks/<id>/ – retrieve a task

PUT/PATCH /api/tasks/<id>/ – update a task

DELETE /api/tasks/<id>/ – delete a task

POST /api/tasks/<id>/complete/ – mark task as complete

POST /api/tasks/<id>/incomplete/ – mark task as incomplete

Query Features

Filtering:

/api/tasks/?status=pending

/api/tasks/?priority=high

Search:

/api/tasks/?search=meeting

Ordering:

/api/tasks/?ordering=due_date

/api/tasks/?ordering=-created_at

Pagination:

/api/tasks/?page=2

Permissions & Security

Only authenticated users can access the API

Users can only access tasks they own

Object-level permissions enforced using custom permissions

Testing

All endpoints tested using Postman

Authentication, permissions, filtering, search, ordering, and pagination verified


Status

Core backend functionality is complete.
The project is ready for deployment and final review.