class total:
    def __init__(self,n,s):
        self.n = n
        self.s = s
    def isprime(self):
        count = 0
        for i in range(1,self.n+1):
            if self.n%i == 0:
                count = count + 1
        if count == 2:
            print("Yes")
        else:
            print("No")
    def ispalindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = total(12,"SaS")
ob1.isprime()
ob2 = total(14,"Hello")
ob2.ispalindrome()
ob3 = total(13,"SaS")
ob3.isprime()
ob3.ispalindrome()