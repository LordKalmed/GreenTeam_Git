class First:

    def add(self,a,b):
        print("result =", a+b)

    def msg2(self):
        print("Qa")
        self.add(10,20)

X=First()
num1=int(input("number one:"))
num2=int(input("number one:"))
X.add(num1,num2)  