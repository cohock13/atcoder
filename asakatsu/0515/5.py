H,W,D = map(int,input().split())

A = []
for _ in range(H):
    A.append(list(map(int,input().split())))

M = [[0 for _ in range(W)] for i in range(H)]

num = [[] for _ in range(H*W+1)]
for i in range(H):
    for j in range(W):
        num[A[i][j]].append([i,j])

dist = [0]*(H*W+1)

for i in range(D,H*W+1):
    if i <= D:
        continue
    else:
        dist[i] = dist[i-D] + abs(num[i][0][0]-num[i-D][0][0]) + abs(num[i][0][1]-num[i-D][0][1])

##print(dist)
Q = int(input())

for _ in range(Q):
    l,r = map(int,input().split())
    print(dist[r]-dist[l])
    

