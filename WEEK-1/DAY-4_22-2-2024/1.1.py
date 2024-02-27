alpha = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s = input()
d={}
for i in s:
    if i in alpha:
        if i not in d:
            d[i] = 1
        else:
            d[i]+= 1
x = d.keys()
print(d)
if len(x) == 26:
    print("Pangram")
else:
    print("Not a Pangram")
