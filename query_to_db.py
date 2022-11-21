import sqlite3

sql_5_stud_high_avg_all_disc = """
    SELECT s.student_name, round(AVG(m.mark), 2) AS avg_marks  
    FROM students s
    LEFT JOIN marks m ON m.student_id = s.id
    GROUP BY s.student_name, s.id
    ORDER BY avg_marks DESC
    LIMIT 5;
    """

sql_one_stud_high_avg_one_disc = """
    SELECT d.discipline_name, s.student_name, round(AVG(m.mark), 2) AS avg_marks  
    FROM students AS s
    LEFT JOIN marks AS m ON m.student_id = s.id
    LEFT JOIN disciplines d ON d.id = m.discipline_id
    WHERE d.discipline_name = 'Python'
    GROUP BY s.student_name, d.discipline_name 
    ORDER BY avg_marks DESC
    LIMIT 1;
    """

sql_avg_score_in_group_for_one_disc = """
    SELECT d.discipline_name, c.class_name , round(AVG(m.mark), 2) AS avg_marks 
    FROM marks m 
    LEFT JOIN disciplines d ON d.id = m.discipline_id 
    LEFT JOIN students s ON s.id = m.student_id 
    LEFT JOIN classes c ON c.id = s.class_id
    WHERE d.discipline_name = 'Kotlin'
    GROUP BY c.class_name, d.discipline_name
    ORDER BY avg_marks DESC;
    """

sql_current_mark_point_avg = """
    SELECT round(AVG(m.mark), 2) AS avg_marks
    FROM marks m;
    """

sql_what_courses_teach_take = """
    SELECT t.teacher_name, d.discipline_name 
    FROM disciplines d 
    LEFT JOIN teachers t ON t.id = d.teacher_id 
    WHERE t.id = 1
    GROUP BY d.discipline_name;
    """

sql_lst_of_stud_in_class = """
    SELECT s.id, s.student_name, c.class_name 
    FROM students s 
    LEFT JOIN classes c ON s.class_id = c.id 
    WHERE c.id = 2
    ORDER BY s.student_name;
    """

sql_marks_of_stud_in_disc_class = """
    SELECT s.id, s.student_name, d.discipline_name, c.class_name, m.mark, m.mark_date
    FROM marks m 
    LEFT JOIN students s ON s.id = m.student_id 
    LEFT JOIN disciplines d ON d.id = m.discipline_id
    LEFT JOIN classes c ON c.id = s.class_id 
    WHERE c.id = 3 AND d.discipline_name = 'NodeJS'
    ORDER BY mark_date DESC;
    """

sql_marks_of_stud_in_disc_class_last_less = """
    SELECT c.class_name, s.student_name, d.discipline_name, m.mark, m.mark_date  
    FROM marks m 
    LEFT JOIN students s ON s.id = m.student_id 
    LEFT JOIN disciplines d ON d.id = m.discipline_id
    LEFT JOIN classes c ON c.id = s.class_id 
    WHERE c.id = 1 AND d.discipline_name = 'PHP'
    GROUP BY m.mark_date
    ORDER BY m.mark_date DESC
    LIMIT 1;
    """

sql_lst_disc_attended_by_stud = """
    SELECT d.discipline_name, s.student_name
    FROM students s 
    LEFT JOIN marks m ON s.id = m.student_id 
    LEFT JOIN disciplines d ON m.discipline_id = d.id
    WHERE s.id = 13
    GROUP BY d.discipline_name;
    """

sql_lst_disc_teach_read_to_stud = """
    SELECT d.discipline_name, t.teacher_name, s.student_name 
    FROM disciplines d 
    LEFT JOIN teachers t ON t.id = d.teacher_id
    LEFT JOIN marks m ON d.id = m.discipline_id 
    LEFT JOIN students s ON s.id = m.student_id 
    WHERE t.id = 2 AND s.id = 9
    GROUP BY d.discipline_name;
    """

sql_avg_score_given_by_teach_to_stud = """
    SELECT t.teacher_name, s.student_name, round(AVG(m.mark),2) AS avg_marks
    FROM marks m 
    LEFT JOIN disciplines d ON d.id = m.discipline_id
    LEFT JOIN teachers t ON t.id = d.teacher_id
    LEFT JOIN students s ON s.id = m.student_id 
    WHERE t.id = 2
    GROUP BY s.student_name
    ORDER BY avg_marks DESC;
    """

sql_avg_mark_by_teach = """
    SELECT t.teacher_name, round(AVG(m.mark),2) AS avg_marks
    FROM marks m 
    LEFT JOIN disciplines d ON d.id = m.discipline_id
    LEFT JOIN teachers t ON t.id = d.teacher_id
    WHERE t.id = 3
    GROUP BY t.teacher_name;
    """


def get_query(sql, database):
    with sqlite3.connect(database) as conn:
        c = conn.cursor()
        c.execute(sql)
        return c.fetchall()
