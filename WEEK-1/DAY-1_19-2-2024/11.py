t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    if a-c > b-d:
        print("Second")
    elif a-c < b-d:
        print("First")
    else:
        print("Any")
