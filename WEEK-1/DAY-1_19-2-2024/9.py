#approach1
t=int(input()) #pizzas and friends
for i in range(t):
    n,x=map(int,input().split())
    x=n*x
    if x%4==0:
        print(x//4)
    else:
        print((x//4)+1)
