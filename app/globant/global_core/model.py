from app.globant.global_utils.database import Base
from sqlalchemy import Column, String, Boolean, Integer


class Departemnt(Base):
    __tablename__ = 'department'
    id = Column(String, primary_key=True)
    department = Column(String)


class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True)
    job = Column(String)


class HiredEmployees(Base):
    __tablename__ = 'hired_employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(Integer)
    department_id = Column(Integer)
    job_id = Column(Integer)


class ReportGroupHiredEmployees(Base):
    __tablename__ = 'vw_group_hired'
    year = Column(Integer, primary_key=True)
    job = Column(String)
    q1 = Column(String)
    q2 = Column(String)
    q3 = Column(String)
    q4 = Column(String)


class ReportTotalHiredEmployees(Base):
    __tablename__ = 'vw_total_hired'
    year = Column(Integer, primary_key=True)
    id = Column(Integer)
    department = Column(String)
    hired = Column(Integer)


