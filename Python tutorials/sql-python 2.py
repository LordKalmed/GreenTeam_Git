import mysql.connector 

db=mysql.connector.connect( host="Localhost", user="root",password="root", database= "clients")

cursor1=db.cursor()

mainmenu=1

while mainmenu!=3:
    print("M A I N M E N U ")
    print()
    print("1-Data Entry")
    print("2-Data View")
    print("3-Quit")
    print()
    mainmenu=int(input("Enter your Choice:"))

    if mainmenu==1:
        print("Data Entry Screen....................")
        print("_______________________________________")
        cursor1.execute("select ifnull(max(student_id),0)+1 from students")
        studentid=cursor1.fetchone()
        name=input("Enter student name:")
        age=int(input("Enter student age:"))
        course=input("Enter student course:")
        sqlinsert="insert into students value({0},'{1}',{2},'{3}')".format(studentid[0],name,age,course)
        cursor1.execute(sqlinsert)
        db.commit()


    if mainmenu==2:
        print("Reporting Screen....................")
        print()
        submenu=1

        while submenu!=4:
            print("1- All recoords")
            print("2- Specfic age Records")
            print("3- Specfic Subject Records")
            print("4- Go to main menu")
            submenu=int(input("Enter your Choice:"))
            

            if submenu==1:
                sqlquey="select * from students"
                cursor1.execute(sqlquey)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])
                submenu=1
                print()
                print("_____complete____")
                
                



            if submenu==2:
                age=input(" Records of which age's you want to see")
                sqlquey="select * from students where age='{0}'".format(age)
                cursor1.execute(sqlquey)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])
                submenu=1
                print()
                print("_____complete____")
                


            if submenu==3:
                subject=input(" Records of which subject you want to see")
                sqlquey="select * from students where dept='{0}'".format(subject)
                records=cursor1.fetchall()
                for rec in records:
                    print(rec[0],rec[1],rec[2],rec[3])
                submenu=1
                print()
                print("_____complete____")
                