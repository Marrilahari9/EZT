n=int(input())
def temp(n):
    r=n
    c=0
    while r>0:
        c+=1
        r=r//10
    n=(3*pow(10,c))+n
    n=n*10+3
    return n
print(temp(n))