import mysql.connector 

db=mysql.connector.connect( host="Localhost", user="root",password="root", database= "clients")

cursor1=db.cursor()

mainmenu=1

while mainmenu!=3:
    print("M A I N M E N U ")
    print("1-Data Entry")
    print("2-Data View")
    print("3-Quit")
    mainmenu=int(input("Enter your Choice:"))

    if mainmenu==1:
        print("Data Entry Screen....................")
        studentid=cursor1.execute("select max(student-id)+1 from students")
        name=input("The students name? :")
        age=input("The students age? :")
        course=input("The students course? :")
        cursor1.execute("Insert into students values({0},'{1}',{2}, '{3}')".format(studentid,name,age,course))
        db.commit()


    if mainmenu==2:
        print("Reporting Screen....................")
        submenu=1

        while submenu!=4:
            print("1- All recoords")
            print("2- Specfic Department Records")
            print("3- Specfic Subject Records")
            print("4- Go to main menu")
            submenu=int(input("Enter your Choice:"))
            

            if submenu==1:
                sqlquey="select * from students"
                cursor1.execute(sqlquey)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])



            if submenu==2:
                dept=input(" Records of which Department you want to see")
                sqlquey="select * from students where dept='{0}'".format(dept)
                cursor1.execute(sqlquey)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])


            if submenu==3:
                subject=input(" Records of which subject you want to see")
                sqlquey="select * from students where dept='{0}'".format(dept)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])
