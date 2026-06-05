Employee Attendance & Payroll Management System

Objective

A backend application built using FastAPI, SQLAlchemy, and MySQL to manage employees, attendance, and payroll processing.

Tech Stack

* Python 3.x
* FastAPI
* SQLAlchemy
* MySQL
* Pydantic
* JWT Authentication

Features

Employee Management

* Add Employee
* View Employees
* Get Employee by ID
* Update Employee
* Delete Employee (Soft Delete)

Attendance Management

* Mark Daily Attendance
* View Attendance Records
* Employee Attendance History
* Monthly Attendance Report

Payroll Management

* Generate Monthly Salary
* Calculate Salary Based on Attendance
* View Salary History

Business Rules

* Employee must exist before marking attendance
* Attendance can be marked only once per day
* Salary is automatically calculated based on attendance
* Prevent duplicate payroll generation for the same month

Additional Features

* JWT Authentication
* Employee Search
* Department Filter
* Soft Delete
* Swagger API Documentation

API Endpoints

Authentication

* POST /login

Employee

* POST /employee
* GET /employee
* GET /employee/{emp_id}
* PUT /employee/{emp_id}
* DELETE /employee/{emp_id}
* GET /employee/search/{name}
* GET /employee/department/{department}

Attendance

* POST /attendance
* GET /attendance
* GET /attendance/{emp_id}
* GET /attendance/month/{emp_id}/{month}

Payroll

* POST /payroll/{employee_id}/{month}
* GET /payroll
* GET /payroll/{employee_id}

Installation

1. Clone the repository
2. Create virtual environment
3. Install dependencies

bash
pip install -r requirements.txt


4. Configure MySQL database
5. Run the application

bash
uvicorn main:app --reload


6. Open Swagger UI

text
http://127.0.0.1:8000/docs


Author

Tharun
