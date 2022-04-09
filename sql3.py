import sqlite3
connect = sqlite3.connect('school.db') 
cur = connect.cursor()

cur.execute("DROP TABLE IF EXISTS classes")
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("DROP TABLE IF EXISTS subjects")
cur.execute("DROP TABLE IF EXISTS marks")

cur.execute("PRAGMA foriegn_keys=on")

query1 = "CREATE TABLE IF NOT EXISTS classes (id INT NOT NULL PRIMARY KEY, class TEXT, num_of_stud INT, teacher TEXT)"
query2 = "CREATE TABLE IF NOT EXISTS students (id INT NOT NULL PRIMARY KEY, familia TEXT, imya TEXT, otchestvo TEXT, id_classes INT, gender TEXT, age INT, FOREIGN KEY (id_classes) REFERENCES classes (id) ON UPDATE CASCADE)"
query3 = "CREATE TABLE IF NOT EXISTS subjects (id INT NOT NULL PRIMARY KEY, subject TEXT)" 
query4 = "CREATE TABLE IF NOT EXISTS marks (id INT NOT NULL PRIMARY KEY, mark INT, id_students INT, id_subjects INT, FOREIGN KEY (id_subjects) REFERENCES subjects (id) ON UPDATE CASCADE, FOREIGN KEY (id_students) REFERENCES student (id) ON UPDATE CASCADE)"

#query3 = "CREATE TABLE IF NOT EXISTS  (Id INT, class INT, num_of_stud INT, teacher INT,)"
cur.execute(query1)
cur.execute("INSERT INTO classes VALUES(1, '5A', 21, 'Pakhomov Dmitry Davidovich')")
cur.execute("INSERT INTO classes VALUES(2, '9B', 22, 'Pavlov Roman Makarovich')")
cur.execute("INSERT INTO classes VALUES(3, '10A', 19, 'Petrova Nika Alekseevna')")
cur.execute("INSERT INTO classes VALUES(4, '8A', 17, 'Kuzin Daniil Lvovich')")
cur.execute("INSERT INTO classes VALUES(5, '1A', 27, 'Shatilova Tatiana Nikolaevna')")
cur.execute("INSERT INTO classes VALUES(6, '2A', 16, 'Shatilova Tatiana Nikolaevna')")
cur.execute("INSERT INTO classes VALUES(7, '3A', 23, 'Markelov Alexander Vladimirovich')")
cur.execute("INSERT INTO classes VALUES(8, '4A', 19, 'Levina Valentina Svyatoslavovna')")
cur.execute("INSERT INTO classes VALUES(9, '6A', 26, 'Borisova Elizaveta Yaroslavovna')")
cur.execute("INSERT INTO classes VALUES(10, '7A', 20, 'Ilina Milana Timurovna')")
cur.execute("INSERT INTO classes VALUES(11, '8B', 22, 'Goryachev Rostislav Davidovich')")
cur.execute("INSERT INTO classes VALUES(12, '9A', 28, 'Lebedeva Ksenia Nikitichna')")
cur.execute("INSERT INTO classes VALUES(13, '10A', 29, 'Sidorova Stefania Artemovna')")
cur.execute("INSERT INTO classes VALUES(14, '10B', 30, 'Pimenov Oleg Alexandrovich')")
cur.execute("INSERT INTO classes VALUES(15, '11A', 26, 'Pirogova Polina Nikolaevna')")

cur.execute(query2)
cur.execute("INSERT INTO students VALUES(911, 'Kotov', 'Andrew', 'Alexandrovich', 1, 'male', 19)")
cur.execute("INSERT INTO students VALUES(912, 'Sobolev', 'Petya', 'Viktorovich', 2, 'male', 18)")
cur.execute("INSERT INTO students VALUES(913, 'Frolov', 'Anotoliy', 'Vyachaslavovich', 3, 'male', 19)")
cur.execute("INSERT INTO students VALUES(914, 'Volkova', 'Liza', 'Vasilevna', 4, 'female', 19)")
cur.execute("INSERT INTO students VALUES(915, 'Ushinskiy', 'Denis', 'Vladimirovich', 5, 'male', 18)")
cur.execute("INSERT INTO students VALUES(916, 'Brown', 'Cody', 'Mikhailovich', 6, 'male', 15)")
cur.execute("INSERT INTO students VALUES(917, 'Evans', 'Francisco', 'Alexandrovich', 7, 'male', 15)")
cur.execute("INSERT INTO students VALUES(918, 'Wilkerson', 'Vanessa', 'Mikhailovna', 8, 'female', 15)")
cur.execute("INSERT INTO students VALUES(919, 'Hamilton', 'Glen', 'Alekseyevich', 9, 'male', 15)")
cur.execute("INSERT INTO students VALUES(920, 'Hernandez', 'Bob', 'Maksimovich', 10, 'male', 15)")
cur.execute("INSERT INTO students VALUES(921, 'Thomas', 'Velma', 'Danielovna', 11, 'female', 15)")
cur.execute("INSERT INTO students VALUES(922, 'Maxwell', 'Lisa', 'Alekseevna', 12, 'female', 15)")
cur.execute("INSERT INTO students VALUES(923, 'Hart', 'Mary', 'Vladimirovna', 13, 'female', 15)")
cur.execute("INSERT INTO students VALUES(924, 'McCormick', 'Pamela', 'Olegovna', 14, 'female', 15)")
cur.execute("INSERT INTO students VALUES(925, 'Williams', 'Christine', 'Romanovna', 15, 'female', 15)")
cur.execute("INSERT INTO students VALUES(926, 'Gilbert', 'Erika', 'Timofeevna', 16, 'female', 15)")
cur.execute("INSERT INTO students VALUES(927, 'Lee', 'Phillip', 'Ilyich', 17, 'male', 15)")
cur.execute("INSERT INTO students VALUES(928, 'Miller', 'Bernard', 'Yegorovich', 18, 'male', 15)")
cur.execute("INSERT INTO students VALUES(929, 'Moore', 'Henry', 'Vladislavovich', 19, 'male', 15)")
cur.execute("INSERT INTO students VALUES(930, 'Turner', 'Tracy', 'Ivanovna', 20, 'female', 15)")
cur.execute("INSERT INTO students VALUES(931, 'Gutierrez', 'Cathy', 'Alexandrovna', 21, 'female', 15)")
cur.execute("INSERT INTO students VALUES(932, 'Williams', 'Deborah', 'Ivanovich', 22, 'male', 15)")
cur.execute("INSERT INTO students VALUES(933, 'Hardy', 'Aaron', 'Zakharovich', 23, 'male', 15)")
cur.execute("INSERT INTO students VALUES(934, 'Adams', 'Paul', 'Romanovich', 24, 'male', 15)")
cur.execute("INSERT INTO students VALUES(935, 'Waters', 'Matthew', 'Ruslanovich', 25, 'male', 15)")
cur.execute("INSERT INTO students VALUES(936, 'Miller', 'Maria', 'Romanovna', 26, 'female', 15)")
cur.execute("INSERT INTO students VALUES(937, 'Brown', 'Judy', 'Nikolaevna', 27, 'female', 15)")
cur.execute("INSERT INTO students VALUES(938, 'Fowler', 'Darryl', 'Alexandrovich', 28, 'male', 15)")
cur.execute("INSERT INTO students VALUES(939, 'West', 'Andrew', 'Maksimovich', 29, 'male', 15)")
cur.execute("INSERT INTO students VALUES(940, 'Butler', 'Michael', 'Mikhailovich', 30, 'male', 15)")
cur.execute("INSERT INTO students VALUES(941, 'Jenkins', 'Joseph', 'Yegorovich', 31, 'male', 15)")
cur.execute("INSERT INTO students VALUES(942, 'Elliott', 'Crystal', 'Alexeyevna', 32, 'female', 15)")
cur.execute("INSERT INTO students VALUES(943, 'Malone', 'Mary', 'Vsevolodovna', 33, 'female', 15)")
cur.execute("INSERT INTO students VALUES(944, 'Fields', 'Peggy', 'Mikhailovna', 34, 'female', 15)")
cur.execute("INSERT INTO students VALUES(945, 'Perkins', 'Justin', 'Alexandrovich', 35, 'male', 15)")

cur.execute(query3)
cur.execute("INSERT INTO subjects VALUES(601, 'Russian language')")
cur.execute("INSERT INTO subjects VALUES(602, 'English language')")
cur.execute("INSERT INTO subjects VALUES(603, 'Math')")
cur.execute("INSERT INTO subjects VALUES(604, 'PE')")
cur.execute("INSERT INTO subjects VALUES(605, 'Physics')")

cur.execute(query4)
cur.execute("INSERT INTO marks VALUES(112, 2, 11, 601)") #
cur.execute("INSERT INTO marks VALUES(113, 3, 12, 602)") #
cur.execute("INSERT INTO marks VALUES(114, 4, 13, 603)") #
cur.execute("INSERT INTO marks VALUES(115, 4, 14, 604)") #
cur.execute("INSERT INTO marks VALUES(116, 5, 15, 605)") #

#cur.execute("SELECT * FROM classes")
#rows = cur.fetchall() 
#for row in rows:
#    print(row)
#print(" ")

cur.execute("SELECT * FROM students")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT imya, familia, otchestvo FROM students")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM students WHERE age=15 LIMIT 30")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM classes WHERE class<>'5A' AND num_of_stud>25")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT * FROM classes WHERE num_of_stud BETWEEN 20 AND 27")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")



cur.execute("SELECT * FROM classes WHERE teacher<>'Shatilova Tatiana Nikolaevna' AND id>=7 LIMIT 5")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")

cur.execute("SELECT imya, familia, otchestvo FROM students WHERE age<18")
rows = cur.fetchall() 
for row in rows:
    print(row)
print(" ")




#cur.execute("SELECT * FROM subjects")
#ows = cur.fetchall() 
#for row in rows:
#    print(row)
#print(" ")

#cur.execute("SELECT * FROM marks")
#rows = cur.fetchall() 
#for row in rows:
#    print(row)
#print(" ")

#connect.commit()
#connect.close()