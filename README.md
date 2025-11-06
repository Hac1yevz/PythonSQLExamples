AZE
`main.py` faylı aşağıdakı əsas funksiyaları yerinə yetirir:
- **create_database():** Yeni `students.db` adlı SQLite məlumat bazası yaradır və əgər mövcuddursa, köhnəsini silir.
- **create_tables():** Tələbə (`students`) və Kurs (`courses`) cədvəllərini yaradır.
- **insert_data():** İlkin nümunə məlumatları cədvəllərə əlavə edir.
- **sql_update_insert_delete():** Məlumat bazası üzərində **CRUD** əməliyyatlarının (yeni tələbə əlavə etmək, mövcud tələbəni yeniləmək, silmək) nümunəsini göstərir.
- **basic_operations():** JOIN sorğuları, WHERE şərtləri və LIMIT istifadə edərək məlumatları çəkir.
- **aggregate_functions():** COUNT, AVG, MAX, MIN və **GROUP BY** kimi SQL funksiyalarını nümayiş etdirir.
- **select_queries():** Müxtəlif `SELECT` sorğuları ilə məlumat çəkmə prosesini izah edir.

ENG
-The main.py file performs the following key functions:
-create_database(): Creates a new SQLite database named students.db and deletes the old one if it already exists.
-create_tables(): Creates the Students (students) and Courses (courses) tables.
-insert_data(): Adds initial sample data to the tables.
-sql_update_insert_delete(): Demonstrates CRUD operations on the database — adding a new student, updating existing records, and deleting entries.
-basic_operations(): Retrieves data using JOIN queries, WHERE conditions, and LIMIT clauses.
-aggregate_functions(): Demonstrates SQL functions such as COUNT, AVG, MAX, MIN, and GROUP BY.
-select_queries(): Explains how to retrieve data using various SELECT queries.
