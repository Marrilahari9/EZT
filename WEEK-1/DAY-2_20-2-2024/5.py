#approach1
def fact(n):#factorial
    if n==0 or n==1:
        return 1
    else:
        r=n*fact(n-1)
        return r
n=int(input())
print(fact(n))
