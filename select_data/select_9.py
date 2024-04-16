"""Знайти список курсів, які відвідує певний студент."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Grade, Discipline, Student


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def courses_attended_by_student(student_name: str):
    
    courses = (
        session.query(Discipline.name)
        .join(Grade)
        .join(Student)
        .filter(Student.fullname == student_name)
        .all()
    )

    cours_for_student = [f"Student: {student_name}, Course:"]
    
    if courses:
        for course in courses:
            cours_for_student.append("".join(course.name))
    else:
        return f"Student '{student_name}' was not found or is not attending courses."
        
    return cours_for_student