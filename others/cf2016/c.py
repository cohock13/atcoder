from collections import deque
"""
https://tjkendev.github.io/procon-library/python/graph/bfs.html
"""
def bfs(G):
    dist = [-1]*(N+M)
    que = deque([0])
    dist[0] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in G[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
    
    return dist

N,M = map(int,input().split())

graph = [[] for _ in range(N+M)]

for i in range(N):
    KL = list(map(int,input().split()))
    for j in KL[1:]:
        graph[i].append(N+j-1)
        graph[N+j-1].append(i)

ans = bfs(graph)

if -1 in ans[:N]:
    print("NO")
else:
    print("YES")
