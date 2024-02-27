n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break