
from heapq import heappush, heappop
INF = float("inf")
def dijkstra(N, G, s):
    dist = [INF] * N
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist

N = int(input())
edge = [[] for _ in range(N)]

for _ in range(N-1):
    a,b,c = map(int,input().split())
    edge[a-1].append((b-1,c))
    edge[b-1].append((a-1,c))

Q,K = map(int,input().split())

dist = dijkstra(N,edge,K-1)

for _ in range(Q):
    x,y = map(int,input().split())
    print(dist[x-1]+dist[y-1])