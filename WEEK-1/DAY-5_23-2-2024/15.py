class classa:
    def __init__(self,n):
        self.n = n
    def factorial(self):
        print(self.fact(self.n))
    def fact(self,n):
        if n == 1:
            return 1
        else:
            return n * self.fact(n-1)
ob = classa(5)
ob.factorial()