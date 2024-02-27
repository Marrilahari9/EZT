#approach1
t=int(input()) #movie
for i in range(t):
    x,y=map(int,input().split())
    x=x-(y//2)
    print(x)
