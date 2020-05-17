from scipy.sparse.csgraph import bellman_ford

N,M = map(int,input().split())

edge = [[0 for i in range(N)] for _ in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    edge[a-1][b-1] = -c

try:
    dist = bellman_ford(edge)
    print(int(-dist[0][-1]))
except:
    print("inf")

