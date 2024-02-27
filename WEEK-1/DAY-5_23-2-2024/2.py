s = input()
c = 0
ch = input()
for i in range(len(s)):
    if s[i] == ch:
        c = c + 1
print(c)