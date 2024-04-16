# import sqlalchemy
# from sqlalchemy import Column, Integer, String, ForeignKey, Date
# from sqlalchemy.orm import relationship

# from db import Base


# class Group(Base):
#     __tablename__ = 'groups'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(10), unique=True)

# class Teacher(Base):
#     __tablename__ = 'teachers'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     fullname = Column(String(50))

# class Student(Base):
#     __tablename__ = 'students'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     fullname = Column(String(30), unique=True)
#     group_id = Column(Integer, ForeignKey('groups.id'))
#     group = relationship("Group", backref="students")

# class Discipline(Base):
#     __tablename__ = 'disciplines'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(20))
#     teacher_id = Column(Integer, ForeignKey('teachers.id'))
#     teacher = relationship("Teacher", backref="disciplines")

# class Grade(Base):
#     __tablename__ = 'grades'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     discipline_id = Column(Integer, ForeignKey('disciplines.id'))
#     student_id = Column(Integer, ForeignKey('students.id'))
#     grade = Column(Integer)
#     date_of = Column(Date)