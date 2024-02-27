t = int(input())
v = "aeiou"
for i in range(t):
    s = list(input().split())
    vc = 0
    cc = 0
    wc = len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in v:
                    vc = vc + 1
                else:
                    cc = cc + 1
    print(wc,vc,cc)