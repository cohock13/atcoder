from copy import deepcopy

H,W = map(int,input().split())

S = [list(input()) for _ in range(H)]
T = deepcopy(S)

vector = [[1,1],[1,-1],[-1,-1],[-1,1],[0,1],[1,0],[-1,0],[0,-1]]

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            for dx,dy in vector:
                x = i+dx
                y = j+dy
                if 0 <= x < H and 0 <= y < W:
                    T[x][y] = "."

U = deepcopy(T)
V = deepcopy(T)

for i in range(H):
    for j in range(W):
        if U[i][j] == "#":
            for dx,dy in vector:
                x = i+dx
                y = j+dy
                if 0 <= x < H and 0 <= y < W:
                    V[x][y] = "#"

if S == V:
    print("possible")
    for i in T:
        print("".join(i))
else:
    print("impossible")






