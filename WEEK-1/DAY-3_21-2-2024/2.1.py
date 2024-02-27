n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i) == 1:
        print(i,end=" ")