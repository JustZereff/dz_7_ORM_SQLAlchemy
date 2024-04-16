"""Знайти які курси читає певний викладач."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Discipline, Teacher


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def courses_taught_by_teacher(teacher_name: str):
    courses = (
        session.query(Discipline.name)
        .join(Teacher)
        .filter(Teacher.fullname == teacher_name)
        .all()
    )

    teacher_disciplin = []
    
    if courses:
        for course in courses:
            teacher_disciplin.append([f"{teacher_name} the following courses: {course[0]}"])
    elif not teacher_disciplin:
        return f"The {teacher_name} was not found or does not teach any courses."
    
    return teacher_disciplin
