H,W = map(int,input().split())
S = list(list(input()) for _ in range(H))

vector = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

for y in range(H):
    tmp = ""
    for x in range(W):
        ##print(y,x)
        if S[y][x] == "#":
            tmp += "#"
        else:
            cnt = 0
            for s,t in vector:
                dx = x + s
                dy = y + t
                if 0 <= dx <= W-1 and 0 <= dy <= H-1:
                    if S[dy][dx] == "#":
                        cnt += 1
            tmp += str(cnt)
    print(tmp)

