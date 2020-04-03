N,M = map(int,input().split())

sc = []
for i in range(M):
    s,c = map(int,input().split())
    c = str(c)
    sc.append([s-1,c])

for i in range(10**N+1):
    tmp = str(i)
    flag = False
    count = 0
    if len(tmp) == N:
        for s,c in sc:
            if tmp[s] == c:
                count += 1
        if count == M:
            flag = True
    if flag:
        print(tmp)
        exit()
print(-1)