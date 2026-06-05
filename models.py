from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
    designation = Column(String)
is_deleted = Column(Boolean, default=False)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(String)
    status = Column(String)  # Present / Absent


class Payroll(Base):
    __tablename__ = "payroll"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    month = Column(String)
    present_days = Column(Integer)
    total_salary = Column(Integer)