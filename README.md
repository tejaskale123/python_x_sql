# Python & SQL Learning Project

A comprehensive learning project combining Python database operations with a **professional Django web application** for user management. This workspace contains both standalone scripts for database manipulation and a full-featured Django project with a modern, responsive UI built with **Bootstrap 5**.

---

## 📋 Project Overview

This repository is organized into two main sections:

1. **Standalone Python & SQL Scripts** - Database operations and practice queries
2. **Django User Management Application** - Production-ready web application with professional UI

---

## 🎨 UI Features (Bootstrap 5 Refactor)

- ✅ **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- ✅ **Professional Styling** - Gradient backgrounds, smooth animations, modern cards
- ✅ **Password Visibility Toggle** - Eye icon to show/hide passwords on all auth pages
- ✅ **Accessibility** - Bootstrap icons, semantic HTML, alt text
- ✅ **Form Validation** - Client-side validation with helpful error messages
- ✅ **Alert System** - Auto-dismissing alerts, success/error/info messages
- ✅ **Navigation Bar** - Sticky navbar with dropdown menu support
- ✅ **Mobile Optimized** - Touch-friendly buttons and spacing

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
└── 📁 Django Application (Django_app/)
    ├── manage.py                  # Django management script
    ├── db.sqlite3                 # SQLite database
    ├── myproject/
    │   ├── settings.py            # Django configuration
    │   ├── urls.py                # URL routing
    │   ├── wsgi.py                # Production server config
    │   └── asgi.py                # Async server config
    ├── users/                     # User management app
    │   ├── models.py              # Database models
    │   ├── views.py               # View controllers
    │   ├── urls.py                # App routes
    │   ├── serializers.py         # API serializers
    │   └── migrations/            # Database migrations
    ├── templates/                 # HTML templates (Bootstrap 5)
    │   ├── base.html              # Base layout with navbar
    │   ├── login.html             # Login page
    │   ├── register.html          # Registration page
    │   ├── dashboard.html         # Main dashboard
    │   ├── users.html             # Users management
    │   ├── profile.html           # User profile
    │   ├── change_password.html   # Password change
    │   └── update.html            # User edit form
    └── static/
        ├── css/
        │   └── style.css          # Professional Bootstrap 5 theme
        └── js/
            └── main.js            # Utility functions
```

---

## ✨ Features

### Django Web Application
- ✅ **User Authentication** - Registration and login (username or email)
- ✅ **Dashboard** - Welcome page with user stats and quick actions
- ✅ **User Management** - Full CRUD operations (Create, Read, Update, Delete)
- ✅ **Profile Management** - View and edit user information
- ✅ **Password Security** - Change password with validation
- ✅ **Session Management** - Secure cookie-based sessions
- ✅ **Responsive UI** - Mobile-first Bootstrap 5 design
- ✅ **Form Validation** - Client and server-side validation
- ✅ **REST API** - API endpoints for user management

### Python Scripts
- ✅ Database connection management
- ✅ Table creation and schema management
- ✅ Data insertion, retrieval, and manipulation
- ✅ JOIN operations for complex queries
- ✅ Data updates and deletion
- ✅ User login system implementation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Conda environment (django_learning)
- MySQL or SQLite
- Modern web browser

### Setup Instructions

#### 1️⃣ Activate Environment
```bash
conda activate django_learning
```

#### 2️⃣ Navigate to Django App
```bash
cd Django_app
```

#### 3️⃣ Install Dependencies
```bash
pip install django djangorestframework django-rest-framework-simplejwt mysql-connector-python
```

#### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

#### 5️⃣ Start Development Server
```bash
python manage.py runserver
```

#### 6️⃣ Access Application
Open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 🌐 Application Routes

| Route | Purpose | Authentication |
|-------|---------|---|
| `/` | Login page | No |
| `/register/` | User registration | No |
| `/dashboard/` | Main dashboard | Yes |
| `/users/` | All users list | Yes |
| `/profile/` | User profile | Yes |
| `/update/<id>/` | Edit user | Yes |
| `/change-password/` | Change password | Yes |
| `/delete/<id>/` | Delete user | Yes |
| `/logout/` | Logout | Yes |

---

## 🎯 Key UI Components

### Authentication Pages
- **Centered Card Layout** - Professional login and registration forms
- **Password Toggle** - Eye icon to show/hide passwords
- **Gradient Background** - Modern purple gradient design
- **Form Validation** - Real-time error messages
- **Responsive Forms** - Works on all screen sizes

### Dashboard & Admin Pages
- **Sticky Navbar** - Always accessible navigation
- **Dropdown Menu** - Additional options (Change Password, Logout)
- **Card-Based Layout** - Organized information display
- **Responsive Table** - Desktop table view, mobile card view
- **Quick Actions** - Buttons for common operations

### User Profile
- **Avatar Circle** - User initial display
- **Profile Card** - Clean information presentation
- **Status Badge** - Account status indicator
- **Edit Actions** - Quick links to profile actions

---

## 🔐 Security Features

- ✅ **Password Hashing** - Django's PBKDF2 hashing algorithm
- ✅ **CSRF Protection** - Token-based CSRF protection on all forms
- ✅ **SQL Injection Prevention** - ORM parameterized queries
- ✅ **Session Security** - Secure cookie-based sessions
- ✅ **Input Validation** - Server-side form validation
- ✅ **Authentication Required** - Protected routes require login

---

## 🎨 Styling & Theme

- **Framework**: Bootstrap 5.3.0
- **Icons**: Bootstrap Icons 1.11.0
- **Colors**: 
  - Primary: Blue (#0d6efd)
  - Success: Green (#198754)
  - Danger: Red (#dc3545)
  - Info: Cyan (#0dcaf0)

---

## 📱 Browser Compatibility

✅ Chrome (latest)
✅ Firefox (latest)
✅ Safari (latest)
✅ Edge (latest)
✅ Mobile browsers (iOS Safari, Chrome Mobile)

---

## 🐛 Troubleshooting

### Django Server Won't Start
```bash
# Check environment is activated
conda activate django_learning

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Ensure STATICFILES_DIRS is set in settings.py
```

### Database Connection Error
```bash
# Verify MySQL is running
# Check credentials in myproject/settings.py
# Ensure database exists
```

### Port Already in Use
```bash
# Use different port
python manage.py runserver 8001
```

---

## 📚 Technology Stack

- **Backend**: Django 4.2+
- **Database**: MySQL / SQLite
- **Frontend**: Bootstrap 5.3.0, HTML5, CSS3, JavaScript
- **API**: Django REST Framework
- **Authentication**: Django Auth + JWT Tokens
- **Python Version**: 3.8+

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `base.html` | Base template with navbar and footer |
| `login.html` | Login authentication page |
| `register.html` | User registration page |
| `dashboard.html` | Main dashboard with stats |
| `users.html` | Users management interface |
| `profile.html` | User profile display |
| `change_password.html` | Password change form |
| `update.html` | User editing form |
| `style.css` | Professional Bootstrap 5 theme |
| `main.js` | JavaScript utilities and functions |

---

## 🎓 Learning Outcomes

This project demonstrates:
- Python database operations and SQL queries
- Django MVT (Model-View-Template) architecture
- User authentication and authorization
- Bootstrap 5 responsive web design
- HTML forms and validation
- RESTful API design
- Database migrations and schema management

---

## 📄 License

This is a learning project. Feel free to use and modify as needed for educational purposes.

---

## 📞 Project Status

✅ **Status**: Production Ready (April 2026)
✅ **UI**: Fully Refactored with Bootstrap 5
✅ **Features**: All Core Features Implemented
✅ **Testing**: Tested on Latest Browsers
✅ **Performance**: Optimized and Fast

---

**Last Updated**: April 10, 2026
**Version**: 2.0 (Bootstrap 5 Refactor)
**Maintainer**: Development Team

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
