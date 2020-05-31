N,M,T = map(int,input().split())
A = tuple(map(int,input().split()))

from heapq import heappush, heappop
INF = 10**10
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

iki = [[] for _ in range(N)]
kaeri = [[] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().split())
    iki[a-1].append((b-1,c))
    kaeri[b-1].append((a-1,c))

ans = max(max(0,T-i-j)*a for a,i,j in zip(A,dijkstra(N,iki,0),dijkstra(N,kaeri,0)))

print(ans)