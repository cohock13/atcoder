N,T = map(int,input().split())
A = list(int(input()) for _ in range(N))

ans = 0

for i in range(N-1):
    ans += min(T,A[i+1]-A[i])

ans += T

print(ans)