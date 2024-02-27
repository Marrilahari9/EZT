class check:
    def __init__(self,s):
        self.s = s
    def ispalindrome(self):
        if self.s == self.s[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = check("Hello")
ob2 = check("SaS")
ob1.ispalindrome()
ob2.ispalindrome()