# Employee Management System

This is a simple employee management system implemented in Python. It allows you to perform CRUD (Create, Read, Update, Delete) operations on employees stored in a SQLite database.

## Installation


1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
2. Run the main.py file:

    ```bash
    python main.py
    ```

## Features

- **Create**: Add new employees to the database.
- **Read**: Retrieve employee information from the database.
- **Update**: Modify existing employee records.
- **Delete**: Remove employees from the database.
- **Search**: Find employees based on specific criteria such as name, surname, or age.
- **Comparison**: Compare employees based on their ages.

## Files and Structure

- **main.py**: Contains the main program logic.
- **employee.py**: Defines the Employee class with methods for CRUD operations.
- **db.py**: Handles database connection and setup.
- **employees.json**: JSON file containing sample employee data.
- **requirements.txt**: Lists the required Python packages.

## Usage

You can use the provided main.py file to interact with the employee management system. Uncomment the desired function calls within the main() function to perform specific tests or operations.
