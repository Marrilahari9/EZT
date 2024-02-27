n = int(input())
a = list(map(int,input().split()))[:n]
a.sort()
for i in range(n-1):
    if a[i]==a[i+1]:
        print(a[i])
        break