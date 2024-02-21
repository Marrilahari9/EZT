
#approach2
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    ts=n*x
    tp=0
    while ts>=4:
        tp=tp+1
        ts=ts-4
    if tp==0:
        print(tp)
    else:
        print(tp+1)
