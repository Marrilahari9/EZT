class classa:
    def factorial(self,n):
        r = 1
        for i in range(1,n+1):
            r = r * i
        print(r)
ob = classa()
ob.factorial(5)