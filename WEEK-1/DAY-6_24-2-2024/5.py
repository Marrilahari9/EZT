class dob:
    def __init__(self,date,month,year):
        self.date=date
        self.month = month
        self.year = year
    def display1(self):
        d = {1:"Jan",2:"Feb"}
        print(self.date)
        print(d[self.month])
        print(self.year)
class details(dob):
    def __init__(self,name,age,date,month,year):
        self.name = name
        self.age = age
        self.date = date
        self.month = month
        self.year = year
        super().__init__(date,month,year)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.date)
        print(self.month)
        print(self.year)
p = details("abc",27,24,1,2001)
p.display()
p.display1()