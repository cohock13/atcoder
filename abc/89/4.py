##解答を見た 手前でO(H^2W^2) ~O(10^9)くらいのことをしていた
H,W,D = map(int,input().split())
A = []
for i in range(H):
    A.append(list(map(int,input().split())))

pos = [[0 for i in range(2)] for j in range(H*W+1)]

for i in range(H):
    for j in range(W):
        pos[A[i][j]][0] = i+1
        pos[A[i][j]][1] = j+1

dist = []
for i in range(1,H*W+1):##O(HW)
    if i<=D:
        dist.append(0)
    else:
        dist.append(dist[i-D-1]+abs(pos[i][0]-pos[i-D][0])+abs(pos[i][1]-pos[i-D][1]))

LR = []
Q = int(input())
for i in range(Q):
    L,R = map(int,input().split())
    LR.append([L,R])

for i in range(Q):
    print(dist[LR[i][1]-1]-dist[LR[i][0]-1])
