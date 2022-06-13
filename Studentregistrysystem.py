import random
import mysql.connector

# connect to mysql db
mydb = mysql.connector.Connect(
    host="localhost",
    username="root",
    password="",
    database="school"
)
print("connected to db")

mycursor = mydb.cursor()



student_id = "STU" + str(random.randrange(1000000, 9999999))
student_firstname = str.upper(input("What is the first name of the student? "))
student_lastname = str.upper(input("What is the last name of the student? "))
student_address = str.upper(input("What is the address of the student? "))
student_email = str.upper(input("What is the email of the student? "))
student_phonenumber = str.upper(input("What is the phonenumber of the student? "))

sql = "INSERT INTO student  (studentID,firstname,lastname,address,email,phonenumber) VALUES (%s,%s,%s,%s,%s,%s)"
val = (student_id, student_firstname,  student_lastname, student_address, student_email, student_phonenumber)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
