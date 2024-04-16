"""Знайти середній бал у групах з певного предмета."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Grade, Discipline, Group, Student


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def avg_grade_by_group(discipline_name: str):

    avg_grades = (
        session.query(Group.name, func.avg(Grade.grade).label('average_grade'))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .filter(Discipline.name == discipline_name)
        .group_by(Group.name)
        .all()
    )

    group_avg = []
    
    for group_name, average_grade in avg_grades:
        group_avg.append([f"Group: {group_name}, Discipline: {discipline_name}, AVG: {average_grade}"]) 

    return group_avg
