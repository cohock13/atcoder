def search(i,j):
    res = 0
    for dx,dy in vec:
        x = i+dx
        y = j+dy

        if 0 <= x < H and 0 <= y < W:
            res += int(m[x][y] == "#") 
    return res
    
H,W = map(int,input().split())

m = [input() for _ in range(H)]

vec = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]

for i in range(H):
    tmp = ""
    for j in range(W):
        if m[i][j] == "#":
            tmp += "#"
        else:
            tmp += str(search(i,j))
    print(tmp)
