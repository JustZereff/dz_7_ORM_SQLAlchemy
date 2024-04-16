"""Знайти список студентів у певній групі."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Student, Group


engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def students_in_group(group_name: str):
    
    students = (
        session.query(Student)
        .join(Group)
        .filter(Group.name == group_name)
        .all()
    )

    students_group_list = []
    
    if students:
        for student in students:
            students_group_list.append([f"Student: {student.fullname}, Group: {group_name} "])
    elif not students_group_list:
        return f"Group '{group_name}' not found or there are no students in it."
    
    return students_group_list