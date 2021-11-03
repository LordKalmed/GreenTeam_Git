class address:
    myaddress=""
    def setaddress(self,addr):
        self.myaddress=addr

class cv:
    def personalinfo(self,name,city,postcode,country):
        self.name=name
        self.address=address()
        self.address.myaddress=city+" "+postcode+" "+country

    def displayCV(self):
        print("Name:", self.name)
        print("Address:", self.address.myaddress)

angus=cv()
angus.personalinfo("Angus", "London", "SW12ex7", "UK")
angus.displayCV()