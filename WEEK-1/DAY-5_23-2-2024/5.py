s = input()
d = "0123456789"
c = 0
for i in s:
    if i in d:
        c = c + 1
if c == len(s):
    print("Yes")
else:
    print("No")