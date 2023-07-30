from pydantic import BaseModel
from typing import Optional


class Department(BaseModel):
    id: int
    department: str

    class Config:
        orm_mode = True


class Job(BaseModel):
    id: int
    job: str

    class Config:
        orm_mode = True


class HiredEmployees(BaseModel):
    id: int
    name: str
    datetime: int
    department_id: int
    jobs_id: int

    class Config:
        orm_mode = True


class ReportGroupHiredEmployees(BaseModel):
    year: int
    department: str
    job: str
    q1: str
    q2: str
    q3: str
    q4: str

    class Config:
        orm_mode = True

class ReportTotalHiredEmployees(BaseModel):
    year: int
    department: str
    id: int
    hired: int

    class Config:
        orm_mode = True
