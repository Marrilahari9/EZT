t=int(input()) #chocolates sharing
for i in range(t):
    n,x=map(int,input().split())
    if(n>x):
        k=n-x
        if k%4==0:
          print(k//4)
        else:
          print((k//4)+1)
    else:
        print(0)
