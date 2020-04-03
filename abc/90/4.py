N,K = map(int,input().split())
ans = 0

if K == 1:
    ans = N**2
else:
    for b in range(K,N+1):
        d = N//b
        r = N%b
        ans += d*max(0,b-K) + max(0,r-K+1)

print(ans)