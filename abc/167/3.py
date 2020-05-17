N,M,X = map(int,input().split())
ca = []

for i in range(N):
    ca.append(list(map(int,input().split())))

ans = 1e10


for i in range(2**N):
    flag = True
    sanko = [0]*M
    cost = 0
    for j in range(N):
        tmp = 0
        if (i>>j)&1:
            cost += ca[j][0]
            for h in range(1,M+1):
                sanko[h-1] += ca[j][h]
    for s in sanko:
        if s < X:
            flag = False
            break
    if flag:
        ans = min(ans,cost)

if ans == 1e10:
    print(-1)
else:
    print(ans)

