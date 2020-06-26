from scipy.sparse.csgraph import dijkstra

N = int(input())
m = list(input() for _ in range(N))

edge = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        edge[i][j] = int(m[i][j])

d = dijkstra(edge)
m = 0
for i in d:
    m = max(m,int(max(i)))

print(m+1)