from collections import deque

H,W = map(int,input().split())

Cx,Cy = map(int,input().split())
Cx,Cy = Cx-1,Cy-1
Dx,Dy = map(int,input().split())
Dx,Dy = Dx-1,Dy-1
S = [input() for _ in range(H)]
vec = [(1,0),(0,1),(-1,0),(0,-1)]
visited = [[0 for i in range(W)] for j in range(H)]
costs = [[0 for i in range(W)] for j in range(H)]


## "#"でも進むものとする．

que = deque()





    

