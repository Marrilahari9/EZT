s = input()
vc = 0
cc = 0
v = "aeiouAEIOU"
for i in s:
    if i.isalpha():
        if i in v:
            vc = vc + 1
        else:
            cc = cc + 1
print(vc,cc)