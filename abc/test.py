n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
dp=[[0,0,0] for _ in range(n)]
dp[0]=l[0]
for i in  range(1,n):
    dp[i][0]=l[i][0]+max(dp[i-1][1],dp[i-1][2])
    dp[i][1]=l[i][1]+max(dp[i-1][0],dp[i-1][2])
    dp[i][2]=l[i][2]+max(dp[i-1][0],dp[i-1][1])
print(max(dp[-1]))