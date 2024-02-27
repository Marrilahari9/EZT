n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    c = a.count(i)
    if c > 1:
        print(i)
        break