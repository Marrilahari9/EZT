t = int(input())
for i in range(t):
    a,b = input().split()
    r = ""
    for j in b:
        if j not in a:
            r = r + j
    print(r)