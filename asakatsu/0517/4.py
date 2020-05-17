from scipy.sparse.csgraph import floyd_warshall
from copy import deepcopy

def check(a):
    dist = floyd_warshall(a)

    for i in dist:
        if float("inf") in i:
            return True
    return False

N,M = map(int,input().split())

edge = [[float("inf") for i in range(N)] for j in range(N)]


ab = []
for _ in range(M):
    a,b = map(int,input().split())
    ab.append((a,b))
    edge[a-1][b-1] = 1
    edge[b-1][a-1] = 1

ans = 0
for a,b in ab:
    tmp = deepcopy(edge)
    tmp[a-1][b-1] = float("inf")
    tmp[b-1][a-1] = float("inf")

    if check(tmp):
        ans += 1

print(ans)

