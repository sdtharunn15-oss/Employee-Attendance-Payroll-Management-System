from sqlalchemy.orm import Session
from models import Employee, Attendance, Payroll



def create_employee(db: Session, data):
    emp = Employee(
        name=data.name,
        email=data.email,
        department=data.department,
        designation=data.designation
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def get_employees(db, skip=0, limit=10):
    return (
        db.query(Employee)
        .filter(Employee.is_deleted == False)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()


def update_employee(db: Session, emp_id: int, data):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        return {"error": "Employee not found"}

    emp.name = data.name
    emp.email = data.email
    emp.department = data.department
    emp.designation = data.designation

    db.commit()
    db.refresh(emp)
    return emp


def delete_employee(db, emp_id):
    employee = db.query(Employee).filter(Employee.id == emp_id).first()

    if not employee:
        return {"message": "Employee not found"}

    employee.is_deleted = True

    db.commit()

    return {"message": "Employee deleted successfully"}

# ---------------- ATTENDANCE ----------------

def mark_attendance(db: Session, data):
    existing = db.query(Attendance).filter(
        Attendance.employee_id == data.employee_id,
        Attendance.date == data.date
    ).first()

    if existing:
        return {"error": "Attendance already marked for this day"}

    att = Attendance(
        employee_id=data.employee_id,
        date=data.date,
        status=data.status
    )

    db.add(att)
    db.commit()
    db.refresh(att)
    return att


def get_attendance(db: Session):
    return db.query(Attendance).all()


def get_attendance_by_employee(db: Session, emp_id: int):
    return db.query(Attendance).filter(Attendance.employee_id == emp_id).all()


def get_monthly_attendance(db: Session, emp_id: int, month: str):
    return db.query(Attendance).filter(
        Attendance.employee_id == emp_id,
        Attendance.date.like(f"{month}%")
    ).all()


# ---------------- PAYROLL ----------------

def generate_payroll(db: Session, employee_id: int, month: str):
    attendance = db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.date.like(f"{month}%"),
        Attendance.status == "Present"
    ).all()

    present_days = len(attendance)

    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        return {"error": "Employee not found"}

    daily_salary = 1000  # simple rule
    total_salary = present_days * daily_salary

    payroll = Payroll(
        employee_id=employee_id,
        month=month,
        present_days=present_days,
        total_salary=total_salary
    )

    db.add(payroll)
    db.commit()
    db.refresh(payroll)

    return payroll


def get_payrolls(db: Session):
    return db.query(Payroll).all()


def get_payroll_by_employee(db: Session, employee_id: int):
    return db.query(Payroll).filter(Payroll.employee_id == employee_id).all()


def search_employee(db, name):
    return db.query(Employee).filter(
        Employee.name.like(f"%{name}%"),
        Employee.is_deleted == False
    ).all()


def filter_department(db, department):
    return db.query(Employee).filter(
        Employee.department == department,
        Employee.is_deleted == False
    ).all()