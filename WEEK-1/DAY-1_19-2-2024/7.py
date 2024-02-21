n=int(input())#flat discount cheaper one
for i in range(n):
    A,B,C,D=map(int,input().split())
    if ((A-C)>(B-D)):
        print("second")
    elif (A-C)<(B-D):
        print("first")

    else:
        print("any")
