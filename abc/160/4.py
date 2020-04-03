import heapq

def dijkstra_heap(s,edge):
    #始点sから各頂点への最短距離
    d = [10**10]*n
    used = [True] * n #True:未確定
    d[s] = 0
    used[s] = False
    edgelist = []
    for a,b in edge[s]:
        heapq.heappush(edgelist,a*(10**6)+b)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        #まだ使われてない頂点の中から最小の距離のものを探す
        if not used[minedge%(10**6)]:
            continue
        v = minedge%(10**6)
        d[v] = minedge//(10**6)
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist,(e[0]+d[v])*(10**6)+e[1])
    return d

################################
N,X,Y = map(int,input().split())
n = N
w = N

edge = tuple([] for i in range(n))
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w):
    if i == 0:
        edge[i].append([1,i+1])
    elif i == w-1:
        edge[i].append([1,i-1])
    else:
        edge[i].append([1,i+1])
        edge[i].append([1,i-1])
edge[X-1].append([1,Y-1])
edge[Y-1].append([1,X-1])

ans = [0]*(N+1)
tmp = []
for i in range(N):
    tmp.append(dijkstra_heap(i,edge)[i+1:])

for i in range(N):
    for j in tmp[i]:
        ans[j] += 1

for i in range(1,N):
    print(ans[i])
