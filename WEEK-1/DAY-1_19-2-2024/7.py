n = int(input())
if n > 0:
    res=0
    while n > 0:
        r = n%10
        res = (res*10)+r
        n = n//10
    print(res)
elif n == 0:
    print(n)
else:
    res=0
    n=n*-1
    while n > 0:
        r = n%10
        res = (res*10)+r
        n = n//10
    print(-1*res)
'''