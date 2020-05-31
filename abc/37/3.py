N,K = map(int,input().split())
a = list(map(int,input().split()))

s = 0
csum = [0]*(N+1)
for i in range(N):
    s += a[i]
    csum[i+1] = s

ans = 0
for i in range(N-K+1):
    ans += csum[K+i] - csum[i]

print(ans)

