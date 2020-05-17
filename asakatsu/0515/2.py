N,K = map(int,input().split())
h = [int(input()) for _ in range(N)]
h.sort()
ans = 1e10
for i in range(N-K+1):
    ans = min(ans,h[i+K-1]-h[i])

print(ans)