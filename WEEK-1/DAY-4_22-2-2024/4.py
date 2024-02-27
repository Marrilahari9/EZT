n = int(input())
d = {}
for i in range(n):
    s = input()
    if s in d:
        d[s] = d[s]+1
    else:
        d[s] = 1
#print(d)
x = max(d.values())
z = []
for i in d:
    if d[i] == x:
        z.append(i)
print(max(z),x)