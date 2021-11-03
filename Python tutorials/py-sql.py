
import mysql.connector

db=mysql.connector.connect( host="Localhost", user="root",password="root", database= "clients")

cursor1=db.cursor()


choice="Y"
while choice =="Y" or choice=="y":

    cursor1.execute("select ifnull(max(student_id),0)+1 from students")
    regno=cursor1.fetchone()

    name=input("Enter student name:")
    age=int(input("Enter student age:"))
    course=input("Enter student course:")

    sqlinsert="insert into students value({0},'{1}',{2},'{3}')".format(regno[0],name,age,course)
    
    cursor1.execute(sqlinsert)

    choice=input("Do you want to enter more data? (Y/N):")

db.commit()

