
import sys
sys.setrecursionlimit(10**8)
 
vector = [(0,-1),(-1,0),(1,0),(0,1)]
mod = 10**9 + 7
 
H,W = map(int,input().split())
a = [tuple(map(int,input().split())) for _ in range(H)]
dist = [[-1 for i in range(W)] for j in range(H)]
 
def calc_dist(i,j):
 
    if dist[i][j] != -1:
        return dist[i][j]
    
    res = 1
    for dx,dy in vector:
        x = i+dx
        y = j+dy
        if 0 <= x < H and 0 <= y < W:
            if a[i][j] < a[x][y]:
                res += calc_dist(x,y)
                res %= mod
    dist[i][j] = res%mod
 
    return res    
 
ans = 0
for i in range(H):
    for j in range(W):
        ans = (ans+calc_dist(i,j))%mod
 
print(ans%mod)