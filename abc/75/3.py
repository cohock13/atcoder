from copy import deepcopy

def warshallfloyd(cost,V):
    INF = float("inf")
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if cost[i][k]!=INF and cost[k][j]!=INF:
                    cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

    for i in cost:
        if float("inf") in i:
            return False
    
    return True

N,M = map(int,input().split())
edge = [[float("inf") for i in range(N)] for j in range(N)]
ab = []
for _ in range(M):
    a,b = map(int,input().split())
    ab.append([a-1,b-1])
    edge[a-1][b-1] = 1
    edge[b-1][a-1] = 1

ans = 0

for a,b in ab:
    tmp = deepcopy(edge)
    tmp[a][b] = float("inf")
    tmp[b][a] = float("inf")
    if not warshallfloyd(tmp,N):
        ans += 1

print(ans)
