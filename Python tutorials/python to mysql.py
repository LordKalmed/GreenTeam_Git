import mysql.connector

db=mysql.connector.connect( host="Localhost", user="root",password="root", database= "clients")

cursor1=db.cursor()

cursor1.execute("Insert into students values(5,'DonkeyKong',26, 'Online')")

db.commit()

