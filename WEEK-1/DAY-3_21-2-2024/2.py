n=int(input())
l=list(map(int,input().split()))[:n]
unique=[]
for i in range(n):
    if l.count(l[i])==1:
        if l[i] in unique:
            continue
        else:
            unique.append(l[i])

for i in unique:
    print(i,end=" ")