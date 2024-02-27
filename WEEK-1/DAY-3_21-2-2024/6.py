t = int(input())
for ii in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    happy = 0
    for i in range(n):
        if a[i] <= 2*bob[i] and b[i]<=2*a[i]:
            happy += 1
    print(happy)