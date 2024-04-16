"""first_rev2

Revision ID: 6d1c6c82b3ef
Revises: dcca4c8f0b48
Create Date: 2024-04-15 22:21:51.730453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime, timedelta
from random import randint

from db import Student, Discipline
# revision identifiers, used by Alembic.
revision: str = '6d1c6c82b3ef'
down_revision: Union[str, None] = 'dcca4c8f0b48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Отримуємо об'єкт метаданих бази даних
    metadata = sa.MetaData()

    # Структура таблиці grades
    grades_table = sa.Table(
        'grades',
        metadata,
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('discipline_id', sa.Integer()),
        sa.Column('student_id', sa.Integer()),
        sa.Column('grade', sa.Integer()),
        sa.Column('date_of', sa.Date()),
        sa.ForeignKeyConstraint(['discipline_id'], ['disciplines.id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'])
    )


    # Генерація оцінок та додаткових даних
    engine = op.get_bind()
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    start_date = datetime.now() - timedelta(days=365)  
    end_date = datetime.now() 

    grade_insert_query = text(
    "INSERT INTO grades (discipline_id, student_id, grade, date_of) "
    "VALUES (:discipline_id, :student_id, :grade, :date_of)"
    )

    for student_id, discipline_id in session.query(Student.id, Discipline.id):
        grade_value = randint(1, 100)
        grade_date = fake.date_time_between(start_date=start_date, end_date=end_date)
        
        session.execute(grade_insert_query, {
            "discipline_id": discipline_id,
            "student_id": student_id,
            "grade": grade_value,
            "date_of": grade_date
        })

    session.commit()

def downgrade():
    # Отримуємо об'єкт метаданих бази даних
    metadata = sa.MetaData()

    # Видаляємо оцінки з таблиці grades
    engine = op.get_bind()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Видаляємо всі рядки з таблиці grades
    session.execute("DELETE FROM grades")

    session.commit()
