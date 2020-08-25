from bisect import bisect,bisect_left
from collections import defaultdict

R,C,K = map(int,input().split())
N = int(input())
rc = []
x = [0]*R
y = [0]*C
memo = defaultdict(int)

for _ in range(N):
    r,c = map(int,input().split())
    r,c = r-1,c-1
    x[r] += 1
    y[c] += 1
    rc.append((r,c))

xx = sorted(x)
yy = sorted(y)

ans = 0
for i in xx:
    ans += bisect(yy,K-i)-bisect_left(yy,K-i)

for r,c in rc:
    ans += (x[r]+y[c]-1) == K
    ans -= (x[r]+y[c]) == K
    ##print(r,c,x[r],y[c],x[r]+y[c]==K+1,x[r]+y[c]==K)

print(ans)