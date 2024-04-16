"""Знайти оцінки студентів у окремій групі з певного предмета."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Student, Group, Grade, Discipline


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def grades_in_group_for_discipline(group_name: str, discipline_name: str):

    grades = (
        session.query(Student.fullname, Grade.grade)
        .join(Group)
        .join(Grade)
        .join(Discipline)
        .filter(Group.name == group_name)
        .filter(Discipline.name == discipline_name)
        .all()
    )

    students_grade_list = []
    
    if grades:
        for student, grade in grades:
            students_grade_list.append([f"Student: {student}, Discipline: {discipline_name}, Grade: {grade}, Group: {group_name}"])
    elif not students_grade_list:
        return f"Student grades in group '{group_name}' for subject '{discipline_name}' were not found."
    
    return students_grade_list
