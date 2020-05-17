N,M = map(int,input().split())

from heapq import heappush, heappop
INF = float("inf")
miti = [-1]*N
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
                if miti[t] == -1:
                    miti[t] = v+1
                heappush(que, (dist[t], t))
    return dist

edge = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    edge[a-1].append((b-1,1))
    edge[b-1].append((a-1,1))

dist = dijkstra(N,edge,0)

print("Yes")
for t in miti[1:]:
    print(t)