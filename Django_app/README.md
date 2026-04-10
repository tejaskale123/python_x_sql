# Django User Management System

A premium, role-based user management web application and API built with Django. 

## Features
- **Premium User Interface**: Includes a modern dark-mode, glassmorphism design with dynamic background animations and responsive Bootstrap 5 layout.
- **Authentication & Validation**: Secure user registration, robust login logic (with username or email), and password updates.
- **Role-Based Access Control**: Built-in functionality where only an `admin` role can create, update, or delete users.
- **RESTful API endpoints**: Complete API available for User interactions (`api_users`, `api_create_user`, `api_update_user`, `api_delete_user`, `api_login`). Uses Django Rest Framework.
- **Secure Environment**: Dotenv configuration ensures seamless loading of safe environment variables. MySQL / MariaDB compatibility setup in `settings.py`.

## Technology Stack
- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite / MySQL configuration supported via `os.environ`
- **Frontend:** HTML, Bootstrap 5, Custom CSS with Glassmorphism
- **Environment Management:** Conda (`django_learning` environment)

## Setup & Installation

1. **Activate Environment:**
   Make sure you are running the proper Python environment.
   ```bash
   conda activate django_learning
   ```

2. **Configure Environment Variables:**
   A `.env` file should be populated with the following keys for standard local execution:
   ```env
   DB_NAME=...
   DB_USER=...
   DB_PASSWORD=...
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

3. **Install Dependencies:**
   Ensure required libraries are installed (`django`, `djangorestframework`, `python-dotenv`, `mysqlclient` if using MySQL).

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start Development Server:**
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/`

## Project Structure
- `myproject/` - General project configurations and routing.
- `users/` - User authentication and data management endpoints via standard generic views and REST endpoints.
   - `models.py`: Built-in Django User and auto-created Profile model with role-based features.
   - `views.py`: Enforces standard and API-based user methods (`@api_view`, `@permission_classes`).
- `templates/` - Contains the premium frontend HTML pages.
- `static/css/style.css` - Includes the glassmorphism dark mode aesthetic.
- `export_project.py` - Useful script provided to summarize and extract the Python codebase for sharing or documentation. 

## REST API Documentation

- `GET /api/users/` - Retrieve all users.
- `POST /api/create-user/` - Add a new user (Admin specific).
- `PUT /api/update-user/<id>/` - Update email/username.
- `DELETE /api/delete-user/<id>/` - Erase a user.
- `POST /api/login/` - Login verification.

*All sensitive API endpoints require JWT/Token/Session authentication, configurable in Django REST Framework settings.*
