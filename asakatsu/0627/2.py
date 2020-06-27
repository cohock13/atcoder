H,W = map(int,input().split())
m = [input() for _ in range(H)]
##「離れ小島」がなければよし
vector = [[0,1],[1,0],[-1,0],[0,-1]]

for i in range(H):
    for j in range(W):
        if m[i][j] == "#":
            flag = False
            for dx,dy in vector:
                x = i + dx
                y = j + dy

                if 0 <= x < H and 0 <= y < W:
                    if m[x][y] == "#":
                        flag = True
            if not flag:
                print("No")
                exit()
                
print("Yes") 

