from scipy.sparse.csgraph import dijkstra
import numpy as np 

N,X,Y = map(int,input().split())

edge = tuple([0]*N for i in range(N))

for i in range(N-1):
    edge[i][i+1] = 1
    edge[i+1][i] = 1

edge[X-1][Y-1] = 1
edge[Y-1][X-1] = 1

ans = np.array(dijkstra(edge),dtype="int32")
cnt = [0]*N
for i in range(N):
    for j in ans[i]:
        cnt[j] += 1

for i in range(1,N):
    print(cnt[i]//2)

