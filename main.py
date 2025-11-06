import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE,
            city TEXT,
            course_id INTEGER)
    ''')
    cursor.execute('''
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            instructor TEXT,
            credits INTEGER)
    ''')

def insert_data(cursor):
    students = [
        (1, "Alice Johnson", 20, "alice@gmail.com", "New York", 1),
        (2, "Bob Smith", 19, "bob@gmail.com", "Chicago", 2),
        (3, "Carol White", 21, "carol@gmail.com", "Boston", 1),
        (4, "David Brown", 20, "david@gmail.com", "New York", 2),
        (5, "Emma Davis", 22, "emma@gmail.com", "Seattle", 3)
    ]
    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcie', 2)
    ]
    cursor.executemany("INSERT INTO students VALUES(?,?,?,?,?,?)", students)
    cursor.executemany("INSERT INTO courses VALUES(?,?,?,?)", courses)

def basic_operations(cursor):
    print("-----Select ALL-----")
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

    print("---- SELECT COLUMNS WITH JOIN ----")
    cursor.execute(
        "SELECT name, age, course_name FROM students s "
        "INNER JOIN courses c ON s.course_id = c.id"
    )
    for row in cursor.fetchall():
        print(row)

    print("---- SELECT with WHERE CLAUSE ----")
    cursor.execute("SELECT * FROM students WHERE age = 20")
    for row in cursor.fetchall():
        print(row)

    print("---- SELECT(LIMIT) ----")
    cursor.execute("SELECT * FROM students ORDER BY age DESC LIMIT 2")
    for row in cursor.fetchall():
        print(row)
def sql_update_insert_delete(conn, cursor):
    cursor.execute(
        "INSERT INTO students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com', 'Miami', 4)"
    )
    conn.commit()
    cursor.execute("UPDATE students set age = 26 where id = 6")
    conn.commit()
    cursor.execute("delete from students where id = 6")
    conn.commit()
def aggregate_functions(cursor):
    #1) Count
    print("Aggregate functions: Count")
    cursor.execute("select count(*) from students")
    result = cursor.fetchall()
    print(result[0][0])
    # 2) Average
    print("Aggregate functions: AVG")
    cursor.execute("select avg(age) from students")
    result = cursor.fetchall()
    print(result[0][0])
    #3) MAX MIN
    print("Maximum ve Minimum")
    cursor.execute("select MAX(AGE),MIN(AGE) from students")
    result=cursor.fetchone()
    max_age,min_age=result
    print("Max age:",max_age)
    print("Min age:",min_age)
    #4) Group BY
    print("---Group BY---")
    cursor.execute("select city,count(*) from students group by city")
    records = cursor.fetchall()
    for row in records:
        print(f"Şəhər:{row[0]} Say:{row[1]}")
def select_queries(cursor):
    queries = ["select * from courses", "select instructor,course_name from courses",
               "select * from students where age = 21",
               "select * from students where city = 'Chicago'",
               "select * from students where city in ('New York','Chicago')"]
    tasks = ["Bütün kurs məlumatların çək",
             "Müəllim adı və kurs adın çək",
             "Yaşı 21 olan tələbələri çək",
             "Çikaqoda qalan tələbələri çək",
             "New york ya da Çikaqoda qalan tələbələri çək"]

    for i, j in zip(tasks, queries):
        print("Task:", i)
        print("Query:",j)
        cursor.execute(j)
        result = cursor.fetchall()
        for row in result:
            print(row)

def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_data(cursor)
        conn.commit()
        sql_update_insert_delete(conn, cursor)
        basic_operations(cursor)
        aggregate_functions(cursor)
        select_queries(cursor)
    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
