t = int(input())
for i in range(t):
    n,r = map(int,input().split())
    d = {}
    for j in range(r):
        sid,cid = map(int,input().split())
        if cid not in d:
            d[cid] = [sid]
        else:
            d[cid].append(sid)
    print(d)
    for j in d:
        if len(d[j]) > n and len(set(d[j])==len(d[j]):
            print(f"Scenario #{i+1} : Impossible")
            break
    else:
        print(f"Scenario #{i+1} : Possible")