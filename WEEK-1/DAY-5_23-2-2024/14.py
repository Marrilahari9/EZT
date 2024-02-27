class classa:
    def __init__(self,n):
        self.n = n
        print(n)
    def factorial(self):
        r = 1
        for i in range(1,self.n+1):
            r = r * i
        print(r)
ob = classa(5)
ob.factorial()