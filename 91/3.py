N = int(input())
ab = []
cd = []
for i in range(N):
    a,b = map(int,input().split())
    ab.append([0,a,b,i])
for i in range(N):
    c,d = map(int,input().split())
    cd.append([0,c,d,i])
cover = []
for i in range(N):
    cnt = 0
    cov = [i]
    for j in range(N):
        if ab[j][1] < cd[i][1] and ab[j][2] < cd[i][2]:
            cnt += 1
            cov.append(j)
    cd[i][0] = cnt
    cover.append(cov)


cd.sort()
C = []
for i in range(N):
    tmp = cover[cd[i][3]]
    tmp.pop(0)
    C.append(tmp)
cd_dist = []
for i in range(N):
    dist = []
    if cd[i][0] != 0:
        for j in C[i]:
            d = (ab[j][1]-cd[i][1])**2+(ab[j][2]-cd[i][2])**2
            dist.append([d,j])
        dist.sort(reverse=True)
        cd_dist.append(dist)
    else:
        cd_dist.append([])

flag = [1]*N
ans = 0
for i in range(N):
    for j in C[i]:
        if flag[j]:
            ans += 1
            flag[j] = 0
            break
    ##print(flag)
print(ans)

    