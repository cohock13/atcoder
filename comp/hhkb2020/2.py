H,W = map(int,input().split())

S = [input() for _ in range(H)]

ans = 0
##横
for i in range(H):
    for j in range(W-1):
        ans += (S[i][j] == "." and S[i][j+1] == ".")

##縦
for i in range(H-1):
    for j in range(W):
        ans += (S[i][j] == "." and S[i+1][j] == ".")

print(ans)