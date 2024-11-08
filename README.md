# Lemon Web Application - META Back-End Developer Capstone Project
![Lemon Web Application](restaurant/static/img/logo.png)

## The purpose of the assessments 

The Little Lemon Meta Backend Capstone Project is a comprehensive web application development project where learners build a full-stack restaurant management system. The project simulates a real-world scenario, creating a backend for "Little Lemon," a fictional Mediterranean restaurant. Using Django and Django REST Framework, students implement core functionalities such as managing menus, handling reservations, and enabling user authentication. The project includes working with relational databases, creating RESTful APIs, and ensuring secure and efficient data handling. This capstone project helps learners develop backend skills and gain hands-on experience with essential tools for professional web development.

  
## Stacks / Libraries

- Django 5.1.3 or latest version
- Python 3.13.0 or latest version
- Django Rest Framework
- MySql
- HTML, CSS, JavaScript

## Installation and Setup

1. Clone the repository from [GitHub](https://github.com/yiyd1004/little-lemon-meta-backend).
2. Create and activate a virtual environment. ex) pipenv
   
    ```
    pipenv shell
    pipenv install
    ```
    If the required library is not installed, install them manually.

    ```
    pipenv install django
    pipenv install djangorestframework
    pipenv install mysqlclient
    pipenv install djoser
    ```

4. Set up the MySqlL database and configure the database settings in `settings.py`.

5. Create database

    ```
    mysql -u root -p
    CREATE DATABASE LittleLemon
    ```

7. Apply migrations using the following command:
   
   ```
   python manage.py makemigrations
   python manage.py migrate

   or

   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
   
8. Create a superuser for the Django admin:
   
   ```
   python manage.py createsuperuser

   or
   
   python3 manage.py createsuperuser
   ```
   
9. Run the development server:
    
   ```
   python manage.py runserver

   or
   
   python3 manage.py runserver
   ```
   
10. Access the application in your web browser at http://localhost:8000/.

## Path

- Main restaurant page
  - http://localhost:8000/restaurant/

- Admin page
  - http://localhost:8000/admin/
 
- User/Auth API
  - http://localhost:8000/auth/users/
  - http://localhost:8000/auth/token/login/
  - http://localhost:8000/auth/token/logout/

- Menu Item API
  - http://localhost:8000/menu-items/
  - http://localhost:8000/menu-items/1

- Booking API
  - http://127.0.0.1:8000/booking/
  - http://127.0.0.1:8000/booking/tables/
  - http://localhost:8000/restaurant/bookings/
