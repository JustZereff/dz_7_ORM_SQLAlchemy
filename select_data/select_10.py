"""Список курсів, які певному студенту читає певний викладач."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Grade, Discipline, Student, Teacher


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def courses_taught_by_teacher_to_student(teacher_name: str, student_name: str):
    
    courses = (
        session.query(Discipline.name)
        .join(Grade)
        .join(Student)
        .join(Teacher)
        .filter(Student.fullname == student_name)
        .filter(Teacher.fullname == teacher_name)
        .distinct()
        .all()
    )

    cours_teacher_for_student = [f"List of courses taught by teacher '{teacher_name}' for student '{student_name}':"]
    
    if courses:
        for course in courses:
            cours_teacher_for_student.append("".join(course.name))
    else:
        return f"{teacher_name} was not found or does not teach courses for student {student_name}."

    return cours_teacher_for_student