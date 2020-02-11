import heapq

N,M = map(int,input().split())
A = list(map(int,input().split()))

B = []

for i in A:
    B.append(-i)

heapq.heapify(B)

for i in range(M):
    tmp = heapq.heappop(B)
    heapq.heappush(B,-1*(-tmp//2))

print(-sum(B))




