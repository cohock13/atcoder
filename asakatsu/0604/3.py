N,M = map(int,input().split())

step = [0]*N

for i in range(M):
    a = int(input())
    step[a-1] = 1

mod = int(1e9+7)

dp = [0]*N

if N == 1:
    if step[0]:
        print(0)
    else:
        print(1)
    exit()

if not step[0] and not step[1]:
    dp[0] = 1
    dp[1] = 2
elif step[0] and not step[1]:
    dp[0] = 0
    dp[1] = 1
elif not step[0] and step[1]:
    dp[0] = 1
    dp[1] = 0
else:
    print(0)
    exit()

for i in range(2,N):
    if step[i]:
        continue
    else:
        dp[i] = (dp[i-1] + dp[i-2])%mod
    
print(dp[-1])
