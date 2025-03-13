# To-Do List API

A full-featured task management application built with Django, Django REST Framework, and Bootstrap. This application allows users to create, manage, and track their tasks through both a web interface and a RESTful API.

## Features

- User authentication system
- Create, read, update, and delete tasks
- Filter tasks by status (Pending, In Progress, Completed)
- Task prioritization
- Due date tracking with overdue notifications
- Responsive design with Bootstrap
- RESTful API for programmatic access

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates, Bootstrap 5
- **Database**: SQLite (default), can be configured for PostgreSQL, MySQL, etc.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd todo-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at http://127.0.0.1:8000/

## API Endpoints

The API provides the following endpoints:

### Authentication

- `POST /accounts/login/`: Log in a user
- `POST /accounts/logout/`: Log out a user
- `POST /register/`: Register a new user

### Tasks

- `GET /api/todos/`: List all tasks for the authenticated user
- `POST /api/todos/`: Create a new task
- `GET /api/todos/{id}/`: Retrieve a specific task
- `PUT /api/todos/{id}/`: Update a specific task
- `PATCH /api/todos/{id}/`: Partially update a specific task
- `DELETE /api/todos/{id}/`: Delete a specific task
- `GET /api/todos/by_status/?status=pending`: Filter tasks by status

## API Usage Examples

### Creating a Task

```bash
curl -X POST http://localhost:8000/api/todos/ \
     -H "Content-Type: application/json" \
     -b cookies.txt \
     -d '{"title":"Buy groceries", "description":"Milk, eggs, bread", "status":"pending", "due_date":"2023-12-31T12:00:00"}'
```

### Listing Tasks

```bash
curl -X GET http://localhost:8000/api/todos/ -b cookies.txt
```

### Filtering Tasks by Status

```bash
curl -X GET http://localhost:8000/api/todos/by_status/?status=pending -b cookies.txt
```

### Updating a Task

```bash
curl -X PUT http://localhost:8000/api/todos/1/ \
     -H "Content-Type: application/json" \
     -b cookies.txt \
     -d '{"title":"Buy groceries", "description":"Milk, eggs, bread, cheese", "status":"completed", "due_date":"2023-12-31T12:00:00"}'
```

### Deleting a Task

```bash
curl -X DELETE http://localhost:8000/api/todos/1/ -b cookies.txt
```

## Web Interface

The application also provides a web interface with the following pages:

- `/`: Home page / Task list
- `/todo/new/`: Create a new task
- `/todo/{id}/`: View task details
- `/todo/{id}/edit/`: Edit a task
- `/todo/{id}/delete/`: Delete a task

## Database Schema

The main model is the `Todo` model with the following fields:

- `id`: Auto-incrementing ID
- `title`: Task title
- `description`: Task description (optional)
- `status`: Task status (pending, in_progress, completed)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `due_date`: Due date (optional)

## Future Improvements

1. Add task categories/tags
2. Implement task sharing between users
3. Add task comments
4. Create mobile app integration
5. Add email notifications for approaching due dates
6. Implement task attachments
7. Add task statistics and reporting

## License

[MIT License](LICENSE)

## Acknowledgements

This project was created using:
- Django
- Django REST Framework
- Bootstrap 5
