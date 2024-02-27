#Approach - 1
n = int(input())
d = {}
for i in range(n):
    name,num = input().split()
    d[name] = num
while True:
    s = input()
    if s in d:
        print(f"{s}={d[s]}")
    else:
        print("Not Found")