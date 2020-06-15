from math import ceil
from collections import deque
H,W,K = map(int,input().split())
x,y,s,t = map(int,input().split())
M = [input() for _ in range(H)]

def dfs(x,y,s,t):
    que = deque()
    que.append([x,y,"",0,0])
    distance = [[-1 for i in range(W)] for j in range(H)]
    dxdy = [[1,0,"a"],[-1,0,"b"],[0,1,"c"],[0,-1,"d"]]##4方向
 
    distance[x][y] = 0
 
    while que:
        x,y,houkou,onaji,cnt = que.popleft()
        ##print(houkou,onaji,cnt)
        if x == s and y == t:
            return cnt
        flag = True
        for i,j,p in dxdy:
            dx = x + i
            dy = y + j
            if 0 <= dx <= H-1 and 0 <= dy <= W-1 and M[dx][dy] == ".":
                if p == houkou:
                    if onaji <= K-1:
                        que.append([dx,dy,p,onaji+1,cnt])
                    else:
                        que.append([dx,dy,p,0,cnt+1])
                else:
                    que.append([dx,dy,p,0,cnt+1])
        
    return -1


d = dfs(x-1,y-1,s-1,t-1)
print(d)
                
   
 
