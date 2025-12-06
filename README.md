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
