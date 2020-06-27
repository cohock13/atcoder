N,M = map(int,input().split())

ans = [0]*N
ans[0] = 1
ball = [1]*N

for _ in range(M):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    if ans[x]:
        ans[y] = 1
    ball[x] -= 1
    ball[y] += 1

    if not ball[x]:
        ans[x] = 0

print(sum([i*(j>0) for i,j in zip(ans,ball)]))


