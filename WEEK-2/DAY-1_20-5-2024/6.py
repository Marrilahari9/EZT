s=[1,2,3,4,5,6,7,8,9,10,11,12]
n=3
flag=0
while len(s)>1:
    if flag==0:
        for i in range(n):
            if len(s)>1:
                s.pop(0)
            else:
                break
        flag=1 
    else:
        for i in range(n):
            if len(s)>1:
                s.pop()
            else:
                break
        flag=0
print(s[0])