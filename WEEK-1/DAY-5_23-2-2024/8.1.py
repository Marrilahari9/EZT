t = int(input())
v = "aeiou"
for i in range(t):
    s = input()
    vc = 0
    cc = 0
    for j in s:
        if j.isalpha():
            if j in v:
                vc = vc + 1
            else:
                cc = cc + 1
    wc = len(s.split())
    print(wc,vc,cc)