class SalarySlip:

    salary=0
    name=""

    def info(self,name1,salary1):
        self.salary=salary1
        self.name=name1

    def displaysalary(self):
        tax=self.salary*30/100
        net=self.salary-tax
        print("_______________________")
        print("Name:", self.name)
        print("your tax is=", tax )
        print("your take home is=", net)
        print("_______________________")

obj=SalarySlip()
name=input("Employe name:")
salary=int(input('Employee salary:'))
obj.info(name, salary)
obj.displaysalary()