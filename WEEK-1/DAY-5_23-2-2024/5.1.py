s = input()
d = "0123456789"
c = 0
for i in s:
    if i not in d:
        c = c + 1
if c == 0:
    print("Yes")
else:
    print("No")
