s = input()
v = "aeiou"
c = "qwrtyopsdfghjklmnbcxz"
s = s.lower()
vc = 0
cc = 0
for i in s:
    if i in v:
        vc = vc + 1
    elif i in c:
        cc = cc + 1
print(vc,cc)