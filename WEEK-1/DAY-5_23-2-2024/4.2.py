s = input()
v = "aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")
