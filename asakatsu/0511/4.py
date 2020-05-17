from collections import defaultdict

N,M = map(int,input().split())
a = [int(input()) for _ in range(M)]

kakiko = [[-1,i] for i in range(N)]
domo = [0]*N

for i in range(M):
    kakiko[a[i]-1][0] = i
    domo[a[i]-1] = 1

kakiko.sort(reverse=True)

ans = []

for i,n in kakiko:
    if i >= 0:
        ans.append(n+1)

for i in range(N):
    if not domo[i]:
        ans.append(i+1)

for i in ans:
    print(i)
