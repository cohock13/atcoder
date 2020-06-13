H,W = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(H)]


ans = []
for i in range(H):

    if i%2 == 0:##左->右
        for j in range(W):
            if m[i][j]%2:
                if j == W-1:
                    if i != H-1:
                        ans.append((i+1,j+1,i+2,j+1))
                        m[i+1][j] += 1
                else:
                    ans.append((i+1,j+1,i+1,j+2))
                    m[i][j+1] += 1
    else:##右->左
        for j in reversed(range(W)):
            if m[i][j]%2:
                if j == 0:
                    if i != H-1:
                        ans.append((i+1,j+1,i+2,j+1))
                        m[i+1][j] += 1
                else:
                    ans.append((i+1,j+1,i+1,j))
                    m[i][j-1] += 1

print(len(ans))
for i in ans:
    print(*i)