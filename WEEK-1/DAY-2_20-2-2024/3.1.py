#approach2
t=int(input())
while(t>0):
    x,y=map(int,input().split())
    x=x-(y//2)
    print(x)
    t-=1