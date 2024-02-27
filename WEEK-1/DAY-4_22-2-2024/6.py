n = int(input())
route = {}
for i in range(n):
    c1,c2 = input().split()
    if c1 not in route:
        route[c1] = [c2]
    else:
        route[c1].append(c2)
print(route)
city = input()
if city in route:
    print(*route[city],sep=" ")
else:
    print("None")