from pprint import pprint
from select_data.select_1 import top_five_students
from select_data.select_2 import student_avg_discipline
from select_data.select_3 import avg_grade_by_group
from select_data.select_4 import average_grade
from select_data.select_5 import courses_taught_by_teacher
from select_data.select_6 import students_in_group
from select_data.select_7 import grades_in_group_for_discipline
from select_data.select_8 import average_grade_by_teacher
from select_data.select_9 import courses_attended_by_student
from select_data.select_10 import courses_taught_by_teacher_to_student

#   Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
select_1 = top_five_students() 

#   Знайти студента із найвищим середнім балом з певного предмета. Предмети: Mathematics, Physics, Chemistry, Biology, History, Literature, Geography, Computer Science
select_2 = student_avg_discipline('Chemistry')

#   Знайти середній бал у групах з певного предмета. Предмети: Mathematics, Physics, Chemistry, Biology, History, Literature, Geography, Computer Science
select_3 = avg_grade_by_group('Literature')

#   Знайти середній бал на потоці (по всій таблиці оцінок).
select_4 = average_grade()

#   Знайти які курси читає певний викладач. Викладачі: Christopher Mathews, Gregory Strong, William Barrera
select_5 = courses_taught_by_teacher('Gregory Strong')

#   Знайти список студентів у певній групі. Назви групп: Group A, Group B, Group C
select_6 = students_in_group('Group A')

#   Знайти оцінки студентів у окремій групі з певного предмета. Треба передати Группу і Предмет
select_7 = grades_in_group_for_discipline('Group B', 'Physics')

#   Знайти середній бал, який ставить певний викладач зі своїх предметів. Передати ім'я викладача
select_8 = average_grade_by_teacher('Christopher Mathews')

#   Знайти список курсів, які відвідує певний студент. Передати ім'я студента
select_9 = courses_attended_by_student('Gabriel Oneill')

#   Список курсів, які певному студенту читає певний викладач.
select_10 = courses_taught_by_teacher_to_student('William Barrera', 'Kim Juarez')


if __name__ == "__main__":
    print('1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.')
    pprint(select_1)
    print('-------------------------------------------------------------------------')
    
    print('2. Знайти студента із найвищим середнім балом з певного предмета.')
    print(select_2)
    print('-------------------------------------------------------------------------')
    
    print('3. Знайти середній бал у групах з певного предмета.')
    pprint(select_3)
    print('-------------------------------------------------------------------------')
    
    print('4. Знайти середній бал на потоці (по всій таблиці оцінок).')
    pprint(select_4)
    print('-------------------------------------------------------------------------')
    
    print('5. Знайти які курси читає певний викладач.')
    pprint(select_5)
    print('-------------------------------------------------------------------------')
    
    print('6. Знайти список студентів у певній групі.')
    pprint(select_6)
    print('-------------------------------------------------------------------------')
    
    print('7. Знайти оцінки студентів у окремій групі з певного предмета.')
    pprint(select_7)
    print('-------------------------------------------------------------------------')
    
    print('8. Знайти середній бал, який ставить певний викладач зі своїх предметів.')
    pprint(select_8)
    print('-------------------------------------------------------------------------')
    
    print('9. Знайти список курсів, які відвідує певний студент.')
    pprint(select_9)
    print('-------------------------------------------------------------------------')
    
    print('10. Список курсів, які певному студенту читає певний викладач.')
    pprint(select_10)
    print('-------------------------------------------------------------------------')