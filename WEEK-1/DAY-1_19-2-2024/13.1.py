t = int(input())
for i in range(t):
    n,x = map(int,input().split())
    k = n*x
    if k%4 == 0:
        print(k//4)
    else:
        print((k//4)+1)