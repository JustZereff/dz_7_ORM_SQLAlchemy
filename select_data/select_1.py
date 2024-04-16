"""Запрос на получение 5 студентов с наибольшим средним баллом"""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Base, Student, Grade

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def top_five_students():
    top_students = (
        session.query(Student, func.avg(Grade.grade).label('average_grade'))
        .join(Grade)
        .group_by(Student)
        .order_by(func.avg(Grade.grade).desc())
        .limit(5)
        .all()
    )

    students_list = []
    
    for student, average_grade in top_students:
        students_list.append([f"Student: {student.fullname}, AVG: {average_grade}"])
        
    return students_list