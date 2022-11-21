from create_db import create_db
from insert_db import insert_data
from query_to_db import get_query, sql_5_stud_high_avg_all_disc, sql_one_stud_high_avg_one_disc, \
    sql_avg_score_in_group_for_one_disc, sql_current_mark_point_avg, sql_what_courses_teach_take, \
    sql_lst_of_stud_in_class, sql_marks_of_stud_in_disc_class, sql_marks_of_stud_in_disc_class_last_less, \
    sql_lst_disc_attended_by_stud, sql_lst_disc_teach_read_to_stud, sql_avg_score_given_by_teach_to_stud, \
    sql_avg_mark_by_teach

CREATE_SQL_FILE = 'create_database.sql'
DATA_BASE = 'education.db'

if __name__ == '__main__':
    create_db(CREATE_SQL_FILE, DATA_BASE)
    insert_data(DATA_BASE)
    print(f'5 students with the highest average score in all disciplines: {get_query(sql_5_stud_high_avg_all_disc, DATA_BASE)}')
    print(f'1 student with the highest average score in one discipline: {get_query(sql_one_stud_high_avg_one_disc, DATA_BASE)}')
    print(f'Average score in group for one discipline: {get_query(sql_avg_score_in_group_for_one_disc, DATA_BASE)}')
    print(f'Current average mark point: {get_query(sql_current_mark_point_avg, DATA_BASE)}')
    print(f'What courses teach take: {get_query(sql_what_courses_teach_take, DATA_BASE)}')
    print(f'List of students in class: {get_query(sql_lst_of_stud_in_class, DATA_BASE)}')
    print(f'Marks of students in the discipline class: {get_query(sql_marks_of_stud_in_disc_class, DATA_BASE)}')
    print(f'Marks of student in discipline and class last lesson: {get_query(sql_marks_of_stud_in_disc_class_last_less, DATA_BASE)}')
    print(f'List of disciplines attended by student: {get_query(sql_lst_disc_attended_by_stud, DATA_BASE)}')
    print(f'The list of courses that the teacher reads to the student: {get_query(sql_lst_disc_teach_read_to_stud, DATA_BASE)}')
    print(f'The average mark given by the teacher to the student: {get_query(sql_avg_score_given_by_teach_to_stud, DATA_BASE)}')
    print(f'The average mark given by the teacher: {get_query(sql_avg_mark_by_teach, DATA_BASE)}')

