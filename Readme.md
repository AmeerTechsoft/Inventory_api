# Store Management API

This project is an API for managing the inventory and suppliers of an online store. The API is built using Django and Django REST Framework.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Documentation](#documentation)

## Features

- Inventory management: Add, view, update, and remove items.
- Supplier management: Add, view, and update suppliers.
- Relationships between inventory items and suppliers.
- Authentication using token-based authentication.
- API documentation using Swagger.

## Requirements

- Python 3.7+
- Django 5.0.6
- PostgreSQL
- pip (Python package installer)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/store-management-api.git
   cd store-management-api
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install PostgreSQL:**

   Ensure PostgreSQL is installed and running on your machine. You can download it from the [official website](https://www.postgresql.org/download/).

## Configuration

1. **Create a `.env` file:**

   Create a `.env` file in the root directory of the project with the following content:

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   ```

2. **Update settings.py to use environment variables:**

   Ensure that `settings.py` is configured to use environment variables from the `.env` file:

   ```python
   from decouple import config, Csv

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': config('DATABASE_NAME'),
           'USER': config('DATABASE_USER'),
           'PASSWORD': config('DATABASE_PASSWORD'),
           'HOST': config('DATABASE_HOST', default='localhost'),
           'PORT': config('DATABASE_PORT', default='5432', cast=int),
       }
   }

   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', default=False, cast=bool)
   ```

## Running the Project

1. **Run migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

3. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

4. **Access the admin interface:**

   Visit `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## API Endpoints

- **Inventory Items:**
  - GET /api/items/ - List all items.
  - POST /api/items/ - Create a new item.
  - GET /api/items/{id}/ - Retrieve an item by ID.
  - PUT /api/items/{id}/ - Update an item by ID.
  - DELETE /api/items/{id}/ - Delete an item by ID.

- **Suppliers:**
  - GET /api/suppliers/ - List all suppliers.
  - POST /api/suppliers/ - Create a new supplier.
  - GET /api/suppliers/{id}/ - Retrieve a supplier by ID.
  - PUT /api/suppliers/{id}/ - Update a supplier by ID.
  - DELETE /api/suppliers/{id}/ - Delete a supplier by ID.

## Testing

1. **Run tests:**

   ```bash
   python manage.py test
   ```

## Documentation

1. **API documentation:**

   The API documentation is available at `http://127.0.0.1:8000/swagger/`.

---

Ensure to replace placeholders like `your_secret_key`, `your_database_name`, `your_database_user`, etc., with actual values for your environment.

This README file provides a comprehensive guide to setting up, configuring, running, and testing your Django project.
