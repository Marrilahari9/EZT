t = int(input())
for i in range(t):
    a,b = input().split()
    b = int(b)
    r = ""
    for i in a:
        k = ord(i)+b
        if k > 122:
            k = 96 + (k-122)
            r = r + chr(k)
        else:
            r = r + chr(k)
    print(r)