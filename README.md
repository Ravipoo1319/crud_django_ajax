# Django CRUD Application

This is a simple Django-based project that demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations using the Django framework. The project provides a web application that allows users to interact with a SQLite database by performing these basic CRUD operations. It is a great starting point for those who want to learn or showcase their Django development skills.

## Tech Stack

- **Python**: The project is built using Python, which is the primary programming language for the Django framework.

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It is the core framework used to create this application.

- **HTML and DTL (Django Template Language)**: HTML is used for creating the web interface, and DTL is used to render dynamic content within HTML templates.

- **Ajax**: The project utilizes Ajax (Asynchronous JavaScript and XML) to provide a seamless user experience by performing certain actions without the need for page reloads.

- **SQLite Database**: SQLite is the default database system used in this project. It is a lightweight, serverless, and self-contained database engine, making it perfect for development and testing.

## Features

The project implements the following features:

1. **Create**: Users can add new records to the database by filling out a form with relevant information.

2. **Read**: Users can view a list of existing records in the database, and they can click on a specific record to view its details.

3. **Update**: Users can edit the details of an existing record, and the changes will be reflected in the database.

4. **Delete**: Users can remove a record from the database, which will result in the permanent deletion of that record.

## Installation

To set up this project locally, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/Ravipoo1319/crud_django_ajax.git
   ```

2. **Navigate to the project directory**:
   ```
   cd crud_django_ajax
   ```

3. **Install Virtual Environment and activate it**:
   ```
   pip -m venv <env_name>
   ```

4. **Install django**:
   ```
   pip install django
   ```

5. **Apply database migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```
   python manage.py runserver
   ```

6. Open a web browser and go to `http://localhost:8000` to access the application.

## Usage

- On the homepage, you'll find a list of records from the database.
- You can fill a form with required details and click on submit to create the record.
- To update the existing record you can click on "Edit" button and submit it.
- To delete the record just click on the "Delete" button.
- This project showcases how to use Django forms for data input, Django templates for rendering views, and Ajax for a smoother user experience.

## Contact

If you have any questions or suggestions regarding this project, feel free to contact:

- Ravindra Pawar
- ravindrapawar1315@gmail.com
- Project Repository: [Link to GitHub Repository](https://github.com/Ravipoo1319/crud_django_ajax)

Thank you for checking out this Django CRUD Application! We hope it helps you in your Django development journey.
