import sqlite3
from faker import Faker
from random import randint, choice

STUDENTS = 30
CLASSES = 3
TEACHERS = 3
DISCIPLINES = ['Python', 'JavaScript', 'PHP', 'Kotlin', 'NodeJS']
MARKS = 20

fake = Faker('uk_UA')


def insert_data(database):
    try:
        with sqlite3.connect(database) as connection:
            cursor = connection.cursor()

            sql_classes = 'INSERT INTO classes (class_name) VALUES (?)'
            for _ in range(CLASSES):
                cursor.execute(sql_classes, (fake.bothify(text='Class: ?-##', letters='АБВГ'),))
            class_id = [i[0] for i in cursor.execute('SELECT id FROM classes')]

            sql_students = 'INSERT INTO students (student_name, class_id) VALUES (?, ?)'
            for _ in range(STUDENTS):
                cursor.execute(sql_students, (fake.first_name() + ' ' + fake.last_name(), choice(class_id),))
            student_id = [i[0] for i in cursor.execute('SELECT id FROM students')]

            sql_teachers = 'INSERT INTO teachers (teacher_name) VALUES (?)'
            for _ in range(TEACHERS):
                cursor.execute(sql_teachers, (fake.first_name() + ' ' + fake.last_name(),))
            teacher_id = [i[0] for i in cursor.execute('SELECT id FROM teachers')]

            sql_disciplines = 'INSERT INTO disciplines (discipline_name, teacher_id) VALUES (?, ?)'
            for discipline in DISCIPLINES:
                cursor.execute(sql_disciplines, (discipline, choice(teacher_id),))
            discipline_id = [i[0] for i in cursor.execute('SELECT id FROM disciplines')]

            sql_marks = 'INSERT INTO marks (mark, mark_date, student_id, discipline_id) VALUES (?, ?, ?, ?)'
            for student in student_id:
                for discipline in discipline_id:
                    for _ in range(MARKS):
                        cursor.execute(sql_marks, (randint(4, 12), fake.date_this_year(), student, discipline,))

            connection.commit()
            print('Data inserted!')
    except sqlite3.Error as e:
        print(e)
        connection.rollback()
    finally:
        connection.close()

