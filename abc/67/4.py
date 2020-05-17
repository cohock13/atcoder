import heapq
 
"""
https://juppy.hatenablog.com/entry/2019/02/18/%E8%9F%BB%E6%9C%AC_python_%E3%83%97%E3%83%A9%E3%82%A4%E3%82%AA%E3%83%AA%E3%83%86%E3%82%A3%E3%82%AD%E3%83%A5%E3%83%BC%28heapq%29%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%83%97%E3%83%AA%E3%83%A0%E6%B3%95
"""
 
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
N = int(input())
n = N
w = N
 
edge = tuple([] for i in range(n))
#edge[i] : iから出る道の[重み,行先]の配列
for i in range(w-1):
    a,b = map(int,input().split())
    edge[a-1].append([1,b-1])
    edge[b-1].append([1,a-1])

dist_zero = dijkstra_heap(0,edge)
dist_n = dijkstra_heap(N-1,edge)
"""
print(dist_zero)
print(dist_n)
"""
b = 0
w = 0

for black,white in zip(dist_zero,dist_n):
    if black > white:
        w += 1
    else:
        b += 1

if b > w:
    print("Fennec")
else:
    print("Snuke")   