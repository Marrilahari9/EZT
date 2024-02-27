s = input()
c = 0
ch = input()
for i in range(len(s)):
    if s[i] == ch and i%2==0:
        c = c + 1
print(c)




