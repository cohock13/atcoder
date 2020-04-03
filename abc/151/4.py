from collections import deque
def dfs_2d(H,W,M,start):
    que = deque()
    que.append([start[0],start[1]])
    distance = [[-1 for i in range(W)] for j in range(H)]
    dxdy = [[1,0],[-1,0],[0,1],[0,-1]]##4方向

    distance[start[0]][start[1]] = 0
    
    while que:
        x,y = que.popleft()
        for i,j in dxdy:
            dx = x + i
            dy = y + j
            if 0 <= dx <= H-1 and 0 <= dy <= W-1 and M[dx][dy] != "#" and distance[dx][dy] == -1:
                distance[dx][dy] = distance[x][y] + 1
                que.append([dx,dy])
                
    return max(max(i) for i in distance)

def main():
    H,W = map(int,input().split())
    M = []
    for i in range(H):
        M.append(input())
    ans = 0
    for i in range(H):
        for j in range(W):
            if M[i][j] != "#":
                start = [i,j]
                ans = max(ans,dfs_2d(H,W,M,start))
    print(ans)

if __name__ == "__main__":
    main()
