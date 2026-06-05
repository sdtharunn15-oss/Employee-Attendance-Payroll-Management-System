from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal

import crud
from auth import create_access_token, get_current_user

import schemas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Attendance Payroll System")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/employee")
def add_employee(data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, data)


@app.get("/employee")
def list_employees(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return crud.get_employees(db)


@app.get("/employee/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee(db, emp_id)

@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db, emp_id)

user: str = Depends(get_current_user)


@app.post("/attendance")
def mark_attendance(data: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    return crud.mark_attendance(db, data)


@app.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):
    return crud.get_attendance(db)


@app.get("/attendance/{emp_id}")
def get_employee_attendance(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_attendance_by_employee(db, emp_id)


@app.get("/attendance/month/{emp_id}/{month}")
def monthly_attendance(emp_id: int, month: str, db: Session = Depends(get_db)):
    return crud.get_monthly_attendance(db, emp_id, month)



user: str = Depends(get_current_user)

@app.post("/payroll/{employee_id}/{month}")
def generate_payroll(employee_id: int, month: str, db: Session = Depends(get_db)):
    return crud.generate_payroll(db, employee_id, month)


@app.get("/payroll")
def get_payrolls(db: Session = Depends(get_db)):
    return crud.get_payrolls(db)

REPORT

@app.get("/payroll/{employee_id}")
def payroll_by_employee(employee_id: int, db: Session = Depends(get_db)):
    return crud.get_payroll_by_employee(db, employee_id)

user: str = Depends(get_current_user)

@app.get("/employee/search/{name}")
def search_employee(name: str, db: Session = Depends(get_db)):
    return crud.search_employee(db, name)


@app.get("/employee/department/{department}")
def filter_department(department: str, db: Session = Depends(get_db)):
    return crud.filter_department(db, department)



@app.post("/login")
def login(data: schemas.LoginSchema):

    if data.username == "admin" and data.password == "admin123":

        token = create_access_token(
            {"sub": data.username}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid username or password"
    )