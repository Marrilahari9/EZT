n = int(input())
fc = []
for i in range(1,n+1):
    if n%i == 0:
        fc.append(i)
if len(fc) == 2:
    print('Prime')
else:
    print("Not a Prime")