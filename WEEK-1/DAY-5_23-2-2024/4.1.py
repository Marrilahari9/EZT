s = input()
v = "aeiouAEIOU"
c = 0
for i in s:
    if i not in v:
        c = c + 1
if c==0:
    print("Yes")
else:
    print("No")