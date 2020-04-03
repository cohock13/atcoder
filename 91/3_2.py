##実装のバグがとれぬ　答えを見る

N = int(input())
ab = []
cd = []
for i in range(N):
    a,b = map(int,input().split())
    ab.append([b,a,i])
for i in range(N):
    c,d = map(int,input().split())
    cd.append([c,d,i])

ab.sort()
cd.sort()

ans = 0
flag_ab = [1]*N
for i in range(N):
    pos = -1
    for j in range(N):
        if ab[j][0] < cd[i][1] and ab[j][1] < cd[i][0] and flag_ab[j]:
            pos = max(pos,j)
    if pos != -1:
        flag_ab[pos] = 0
        ans += 1

print(ans)