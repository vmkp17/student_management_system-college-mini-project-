import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vmkp@1701",
    database="student_db"
)

cursor = connection.cursor()
print("Connected Successfully!")
