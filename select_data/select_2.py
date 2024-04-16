"""Знайти студента із найвищим середнім балом з певного предмета."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Base, Student, Grade, Discipline


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def student_avg_discipline(discipline_name: str):

    top_student = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade)
        .join(Discipline)  
        .filter(Discipline.name == discipline_name) 
        .group_by(Student)
        .order_by(func.avg(Grade.grade).desc())
        .first()
    )

    if top_student:
        student, average_grade = top_student
        return f"The student with the highest average score in the subject '{discipline_name}': {student.fullname}, AVG: {average_grade}"
    else:
        return f"No data on students by subject '{discipline_name}'"
