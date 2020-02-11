N,M = map(int,input().split())
a = [1]*N
for i in range(M):
    a[int(input())-1] = 0

mod = int(1e9+7)

dp = [0]*N

if N == 1:
    print(1)
    exit()

if a[0] and a[1]:
    dp[0] = 1
    dp[1] = 2
elif not a[0] and a[1]:
    dp[1] = 1

for i in range(2,N):
    if a[i]:
        dp[i] = dp[i-1] + dp[i-2]
    else:
        dp[i] = 0

print(dp[N-1]%mod)

