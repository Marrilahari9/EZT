t = int(input())
for i in range(t):
    n = int(input())
    factors = []
    for j in range(1,n+1):
        if n%j == 0:
            factors.append(j)
    ef = []
    of = []
    for j in factors:
        if j%2==0:
            ef.append(j)
        else:
            of.append(j)
    if len(ef)==len(of):
        print(1)
    else:
        print(0)