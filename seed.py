from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from faker import Faker
from datetime import datetime, timedelta
from random import randint, choice
from db import Base, Group, Teacher, Student, Discipline, Grade

# Підключення до бази даних
engine = create_engine('postgresql://postgres:postgres@localhost/postgres')
Base.metadata.bind = engine

# Створення сесії
DBSession = sessionmaker(bind=engine)
session = DBSession()

fake = Faker()

# Додавання груп
groups = ['Group A', 'Group B', 'Group C']
for name in groups:
    group = Group(name=name)
    session.add(group)

session.commit()

# Додавання викладачів
for _ in range(3):
    teacher = Teacher(fullname=fake.name())
    session.add(teacher)

session.commit()

# Додавання предметів
disciplines = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Geography', 'Computer Science']
for name in disciplines:
    teacher = session.query(Teacher).order_by(func.random()).first()  # Випадково вибираємо викладача
    discipline = Discipline(name=name, teacher=teacher)
    session.add(discipline)

session.commit()

# Додавання студентів
for _ in range(30):
    student = Student(fullname=fake.name(), group_id=randint(1, 3))
    session.add(student)

session.commit()

# Генерація оцінок
start_date = datetime.now() - timedelta(days=365)  # Стартова дата для генерації оцінок
end_date = datetime.now()  # Кінцева дата для генерації оцінок

for student in session.query(Student):
    for discipline in session.query(Discipline):
        # Генерація випадкової оцінки від 1 до 100
        grade_value = randint(1, 100)
        # Генерація випадкової дати в діапазоні start_date і end_date
        grade_date = fake.date_time_between_dates(start_date=start_date, end_date=end_date)
        # Додавання оцінки до бази даних
        grade = Grade(discipline_id=discipline.id, student_id=student.id, grade=grade_value, date_of=grade_date)
        session.add(grade)

session.commit()
