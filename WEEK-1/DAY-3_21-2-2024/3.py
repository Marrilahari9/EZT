t = int(input())
for i in range(t):
    n = int(input())
    t1 = 0
    t2 = 0
    for j in range(1,n+1):
        if n%j == 0:
            if j%2 == 0:
                t1 = t1 + 1
            else:
                t2 = t2 + 1
    if t1 == t2:
        print(1)
    else:
        print(0)