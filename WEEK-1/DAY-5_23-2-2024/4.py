s = input()
v = "aeiouAEIOU"
c = 0
for i in s:
    if i in v:
        c = c + 1
if c == len(s):
    print("Yes")
else:
    print("No")
