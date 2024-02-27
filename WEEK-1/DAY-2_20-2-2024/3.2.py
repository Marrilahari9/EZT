#approach3
t=int(input())
def test(t):
    if t>0:
        x,y=map(int,input().split())
        x=x-(y//2)
        print(x)
    else:
        return
    test(t-1)
test(t)
