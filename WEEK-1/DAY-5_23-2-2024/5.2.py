s = input()
d = "0123456789"
c = 0
for i in s:
    if i not in d:
        print("No")
        break
else:
    print("Yes")