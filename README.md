# Employee Management System

A simple web-based Employee Management System built using **Django** and **Python** that allows managing employee details efficiently.

## Features

- User authentication (Signup/Login/Logout)
- Admin dashboard to manage employees
- Add, view, update, and delete employee records
- Employee profile details (Name, Email, Employee ID, Gender, etc.)
- Responsive and user-friendly interface
- Secure form handling with validation

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default with Django)
- **Version Control:** Git, GitHub

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-link>
Navigate into the project directory:

cd employee-management-system


Create a virtual environment:

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py migrate


Create a superuser (Admin):

python manage.py createsuperuser


Run the development server:

python manage.py runserver


Access the application at http://127.0.0.1:8000

## Usage
Admin Panel: Manage employees by logging into the Django admin panel at /admin.

Employee Management: Add, edit, view, and delete employee records via the web interface.

Authentication: Users can signup, login, and manage their account securely.
