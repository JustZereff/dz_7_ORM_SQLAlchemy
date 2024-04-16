"""Знайти середній бал, який ставить певний викладач зі своїх предметів."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Grade, Discipline, Teacher


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def average_grade_by_teacher(teacher_name: str):
    
    avg_grade = (
        session.query(func.avg(Grade.grade))
        .join(Discipline)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name)
        .scalar()
    )

    if avg_grade is not None:
        return f"The average grade given by teacher {teacher_name} in his subjects: {avg_grade:.2f}"
    else:
        return f"{teacher_name} was not found or is not grading."