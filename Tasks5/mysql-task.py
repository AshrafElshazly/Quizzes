import mysql.connector as connection

conn = connection.connect(host = "127.0.0.1", user = "root")

mycursor = conn.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS aws")

mycursor.execute("USE aws")

mycursor.execute("CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), degree int(3))")

mycursor.execute("SHOW TABLES")
all = mycursor.fetchall()
print(all)

sql = "INSERT INTO students (name, degree) VALUES (%s, %s)"
val = ("ashraf","100")
mycursor.execute(sql, val)
conn.commit()

case = 'ashraf'
mycursor.execute(f"SELECT * FROM students WHERE name = (%s)",(case,))

all = mycursor.fetchall()
print(all)

# mycursor.execute("DROP DATABASE aws")
conn.close()