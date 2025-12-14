# Task Management API

A backend Task Management system built with Django and Django REST Framework.
This project is part of my Backend Capstone Project.

## Features
- User registration & login
- Create, Read, Update, and Delete tasks
- Mark tasks as complete or incomplete
- Task filtering by status, priority, and due date
- Only the task owner can access their tasks

## Tech Stack
- Django
- Django REST Framework
- SQLite (Development)
- PythonAnywhere / Heroku (Deployment)

## Getting Started
```bash
git clone https://github.com/Hillary-Robert/task-management-api.git
cd task-management-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Progress

So far, the following has been implemented and tested successfully:

### Authentication
- User login using Django REST Framework Token Authentication
- Tokens are generated on login and required for all protected endpoints
- Authentication tested using Postman

### Tasks API
- Authenticated users can:
  - Create a task
  - View all their tasks
- Each task is automatically linked to the logged-in user
- Tasks created by one user are not accessible by other users

### Tested Endpoints
- `POST /api/login/` – returns authentication token
- `GET /api/` – API root (authenticated)
- `GET /api/tasks/` – list user’s tasks
- `POST /api/tasks/` – create a new task

### Tools Used
- Postman for API testing
- Django ORM for database interactions
- SQLite for local development

Further features such as task updates, completion logic, filtering, pagination, testing, and deployment will be implemented in the next phase.
