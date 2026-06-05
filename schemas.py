from pydantic import BaseModel
from typing import Optional



class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    designation: str


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None


class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True



class AttendanceCreate(BaseModel):
    employee_id: int
    date: str        # format: YYYY-MM-DD
    status: str      # Present / Absent / Leave


class AttendanceOut(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True



class PayrollCreate(BaseModel):
    employee_id: int
    month: str   # format: YYYY-MM


class PayrollOut(BaseModel):
    id: int
    employee_id: int
    month: str
    present_days: int
    total_salary: float

    class Config:
        from_attributes = True



class MonthlyAttendanceReport(BaseModel):
    employee_id: int
    month: str
    total_present_days: int


class SalaryReport(BaseModel):
    employee_id: int
    month: str
    present_days: int
    total_salary: float


class LoginSchema(BaseModel):
    username: str
    password: str