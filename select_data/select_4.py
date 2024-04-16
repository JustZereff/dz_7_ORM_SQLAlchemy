"""Знайти середній бал на потоці (по всій таблиці оцінок)."""

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import Grade

engine = create_engine('postgresql://postgres:postgres@localhost/postgres')

Session = sessionmaker(bind=engine)
session = Session()

def average_grade():
    avg_grade = session.query(func.avg(Grade.grade)).scalar()

    return f"Average score for the entire rating table: {avg_grade}"