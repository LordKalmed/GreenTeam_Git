def dosomething(F):
   F()

def msg1():
    print("Hello")

def msg2():
    print("Goodbye")

def whatshouldido(day):
    if day==1:
        def dothis():
            print("Day 1 tasks")
    if day==2:
        def dothis():
            print("Day 2 tasks")
    if day==3:
        def dothis():
            i=0
            while i<=10:
                print(i)
                i+=1
    return dothis


ff=whatshouldido(3)

ff()