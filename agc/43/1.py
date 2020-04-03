import sys, re, os
def input(): return sys.stdin.readline().strip()
##幅優先探索
from collections import deque
 
def dfs(H,W,M):
    que = deque()
    if M[0][0] == "#":
        que.append([0,0,1,1])
    else:
        que.append([0,0,0,0])

    d = [[1,0],[0,1]]
    ans = 0
    
    while que:
        x,y,num_sharp,in_sharp = que.popleft()
        ans += 1

        for i,j in d:
            dx = x + i
            dy = y + j
            if 0 <= dx <= W-1 and 0 <= dy <= H-1:
                if M[dy][dx] == "#" and in_sharp:
                    que.append([dx,dy,num_sharp,1])
                elif M[dy][dx] == "#" and not in_sharp:
                    que.append([dx,dy,num_sharp+1,0])
                else:##M[dx][dy] == "."
                    que.append([dx,dy,num_sharp,0])
        if x == W-1 and y == H-1:
            ans += 0
    return ans
 
 
def main():
    H,W = map(int,input().split())
    M = []
    for i in range(H):
        M.append(list(input()))
    print(dfs(H,W,M))
 
if __name__ == "__main__":
    main()