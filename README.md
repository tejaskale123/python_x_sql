# Python & SQL Learning Project

A comprehensive learning project combining Python database operations with a Django web application for user management. This workspace contains both standalone scripts for database manipulation and a full-featured Django project.

---

## 📋 Project Overview

This repository is organized into two main sections:

1. **Standalone Python & SQL Scripts** - Database operations and practice queries
2. **Django User Management Application** - Full-featured web application

---

## 🗂️ Project Structure

```
python_x_sql/
├── 📄 Database Operation Scripts
│   ├── db_connect.py              # Database connection setup
│   ├── create_table.py            # Create database tables
│   ├── create_orders.py           # Create orders table
│   ├── insert_data.py             # Insert sample data
│   ├── insert_orders.py           # Insert orders data
│   ├── fetch_data.py              # Retrieve data from database
│   ├── fetch_join.py              # JOIN operations
│   ├── update_data.py             # Update records
│   ├── delete_data.py             # Delete records
│   ├── login_system.py            # User login implementation
│   ├── python_test.py             # Test scripts
│   └── practice_queries.sql       # SQL practice queries
│
└── 📁 Django Web Application (myproject/)
    ├── manage.py                  # Django management script
    ├── db.sqlite3                 # SQLite database
    ├── myproject/                 # Project configuration
    │   ├── settings.py            # Django settings
    │   ├── urls.py                # URL routing
    │   ├── wsgi.py                # Production server
    │   └── asgi.py                # Async server
    ├── users/                     # User management app
    │   ├── models.py              # Database models
    │   ├── views.py               # View controllers
    │   ├── urls.py                # App URL routes
    │   ├── serializers.py         # Data serializers
    │   ├── db_config.py           # Database config
    │   ├── migrations/            # Database migrations
    │   └── tests.py               # Unit tests
    ├── templates/                 # HTML templates
    │   ├── login.html
    │   ├── register.html
    │   ├── dashboard.html
    │   ├── profile.html
    │   ├── users.html
    │   ├── change_password.html
    │   └── update.html
    └── static/
        └── css/
            └── style.css          # Responsive styling
```

---

## ✨ Features

### Django Web Application
- ✅ User registration with validation
- ✅ User login (username or email)
- ✅ Dashboard with user summary
- ✅ User profile management
- ✅ Change password functionality
- ✅ User list with full CRUD operations
- ✅ Responsive & clean design
- ✅ Secure password handling

### Python Scripts
- ✅ Database connection management
- ✅ Table creation and schema management
- ✅ Data insertion and retrieval
- ✅ JOIN operations for complex queries
- ✅ Data updates and deletion
- ✅ User login system implementation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Conda or virtualenv
- MySQL or SQLite
- Git (optional)

### Setup Instructions

#### 1️⃣ Activate Environment
```bash
conda activate django_learning
```

#### 2️⃣ Install Dependencies
```bash
pip install django mysql-connector-python
```

---

## 💻 Running Standalone Scripts

### Database Connection Test
```bash
python db_connect.py
```

### Create Tables
```bash
python create_table.py
python create_orders.py
```

### Insert Data
```bash
python insert_data.py
python insert_orders.py
```

### Fetch Data
```bash
python fetch_data.py
python fetch_join.py
```

### Update Records
```bash
python update_data.py
```

### Delete Records
```bash
python delete_data.py
```

### Test Login System
```bash
python login_system.py
```

### Run Tests
```bash
python python_test.py
```

---

## 🌐 Running Django Application

### Step 1: Navigate to Project
```bash
cd myproject
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 4: Start Development Server
```bash
python manage.py runserver
```

### Step 5: Access Application
Open your browser and visit:
```
http://127.0.0.1:8000/
```

### Available Routes
- **Login**: `/login/` - User login page
- **Register**: `/register/` - New user registration
- **Dashboard**: `/dashboard/` - User dashboard
- **Profile**: `/profile/` - User profile
- **Users List**: `/users/` - View all users
- **Update**: `/update/<id>/` - Edit user details
- **Change Password**: `/change-password/` - Change password
- **Logout**: `/logout/` - Logout user

---

## 🗄️ Database Configuration

### For MySQL
Update `myproject/users/db_config.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}
```

Update `myproject/myproject/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### For SQLite (Default)
No configuration needed - uses `db.sqlite3` by default.

---

## 📝 SQL Queries Practice

Refer to `practice_queries.sql` for SQL learning materials including:
- SELECT statements
- JOIN operations
- Aggregate functions
- WHERE clauses
- GROUP BY operations

---

## 🔒 Security Notes

- **Password Hashing**: All passwords are hashed using Django's built-in hashing mechanisms
- **CSRF Protection**: Enabled on all POST requests
- **SQL Injection**: Protected through Django ORM parameterized queries
- **Authentication**: Cookie-based session management
- **Production**: Change `DEBUG=False` in `settings.py` for deployment

---

## 📦 File Descriptions

| File | Purpose |
|------|---------|
| `db_connect.py` | Establishes database connection |
| `create_table.py` | Creates initial database schema |
| `insert_data.py` | Populates database with sample data |
| `fetch_data.py` | Retrieves and displays records |
| `update_data.py` | Modifies existing records |
| `delete_data.py` | Removes records from database |
| `fetch_join.py` | Performs table JOIN operations |
| `login_system.py` | User authentication logic |
| `practice_queries.sql` | SQL learning exercises |

---

## 🐛 Troubleshooting

### Django Server Won't Start
- Ensure environment is activated
- Check `settings.py` for database configuration
- Run `python manage.py migrate` again
- Clear `db.sqlite3` and start fresh if needed

### Database Connection Error
- Verify MySQL/SQLite is running
- Check database credentials in `db_config.py`
- Ensure database exists
- Check network connectivity for MySQL

### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` in `settings.py`
- Verify `static/` folder exists

### Port Already in Use
```bash
python manage.py runserver 8001
```

---

## 📚 Learning Resources

This project covers:
- Python database operations
- SQL queries and joins
- Django MVT architecture
- User authentication
- HTML/CSS templates
- Database migrations
- REST principles (serializers)

---

## 📋 Environment Information

- **Python**: 3.8+
- **Django**: 3.2+
- **Database**: SQLite (default) or MySQL
- **OS**: Windows/Linux/macOS

---

## 📞 Project Timeline

This project demonstrates progression from:
1. Basic database connectivity
2. CRUD operations with Python
3. SQL query practice
4. Full Django application development
5. User management system implementation

---

## 📄 License

This is a learning project. Feel free to use and modify as needed.

---

## ✅ Checklist for First Run

- [ ] Activate conda environment
- [ ] Install dependencies
- [ ] Navigate to `myproject/` folder
- [ ] Run migrations: `python manage.py migrate`
- [ ] Start server: `python manage.py runserver`
- [ ] Open browser to `http://127.0.0.1:8000/`
- [ ] Test registration and login
- [ ] Explore all features

---

**Last Updated**: April 2026  
**Status**: Active Development
