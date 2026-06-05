from sqlalchemy.orm import Session
from models import Attendance


def calculate_salary(db: Session, employee_id: int, month: str):
    records = db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()

    present_days = len([r for r in records if r.status.lower() == "present"])

    daily_salary = 2000
    total_salary = present_days * daily_salary

    return present_days, total_salary