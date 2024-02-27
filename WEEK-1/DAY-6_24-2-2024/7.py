from abc import ABC,abstractmethod
class a(ABC):
    @abstractmethod
    def display(self):
        pass
class b(a):
    def display(self):
        print("Class B")
class c(a):
    def display(self):
        print("Class c")

c1 = c()
c1.display()
c2 = b()
c2.display()