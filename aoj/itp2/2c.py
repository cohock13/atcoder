import heapq
n,q = map(int,input().split())

S = [[] for i in range(n)]
for i in range(q):
    query = tuple(map(int,input().split()))

    if query[0] == 0:
        heapq.heappush(S[query[1]],-1*query[2])
    elif query[0] == 1:
        if len(S[query[1]]) != 0:
            a = heapq.heappop(S[query[1]])
            print(-1*a)
            heapq.heappush(S[query[1]],a)
    else:
        if len(S[query[1]]) != 0:
            heapq.heappop(S[query[1]])
