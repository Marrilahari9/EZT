s = input()
n = len(s)
es = ""
os = ""
for i in range(n):
    if i%2 == 0:
        es = es + s[i]
    else:
        os = os + s[i]
print(os+es)