s = input()
c = 1
r = ""
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        c = c + 1
    else:
        r = r + s[i-1]
        r = r + str(c)
        c = 1
r = r + s[len(s)-1] + str(c)
print(r)