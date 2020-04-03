def ans_dp(H,W,M):
    dp = [[0 for i in range(W)] for j in range(H)]
    flag = [[0 for i in range(W)] for j in range(H)]
    if M[0][0] == "#":
        dp[0][0] = 1
        flag[0][0] = 1
    else:
        dp[0][0] == 0
    for i in range(1,W):
        if M[0][i] == "#":
            flag[0][i] = 1
            if flag[0][i-1] == 1:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = dp[0][i-1] + 1 
        else:##M[0][i] = "."
            dp[0][i] = dp[0][i-1]
    for j in range(1,H):
        if M[j][0] == "#":
            flag[j][0] = 1
            if flag[j-1][0] == 1:
                dp[j][0] = dp[j-1][0]
            else:
                dp[j][0] = dp[j-1][0] + 1 
        else:##M[0][i] = "."
            dp[j][0] = dp[j-1][0]
    
    for i in range(1,H):
        for j in range(1,W):
            if M[i][j] == "#":
                flag[i][j] = 1
                dp[i][j] = min(dp[i-1][j]+int(not flag[i-1][j]),dp[i][j-1]+int(not flag[i][j-1]))
            else:#M[i][j] == "."
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

def main():
    H,W = map(int,input().split())
    M = []
    for i in range(H):
        M.append(list(input()))
    print(ans_dp(H,W,M))
 
if __name__ == "__main__":
    main()