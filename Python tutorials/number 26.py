def tax(salary):
    t=salary*25/100
    return t

salary=int(input("your salary:"))
print("your tax is:", tax(salary))
net=salary-tax(salary)
print("Your net is:", net)
if tax(salary)>700:
    print("too much tax")
else:
    print('nice amount of tax')