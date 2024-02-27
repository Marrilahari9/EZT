class vehicle:
    def __init__(self,fuel):
        self.fuel = fuel
    def display3(self):
        print(self.fuel)
class motor(vehicle):
    def __init__(self,cc,fuel):
        self.cc = cc
        self.fuel = fuel
        super().__init__(fuel)
    def display2(self):
        print(self.cc)
        print(self.fuel)
class car(motor):
    def __init__(self,name,cc,fuel):
        self.name = name
        self.cc = cc
        self.fuel = fuel
        super().__init__(cc,fuel):
    def display1(self):
        print(self.name)
        print(self.cc)
        print(self.fuel)
v1 = car("BMW","300cc","Petrol")
v1.display1()
v1.display2()
v1.display3()