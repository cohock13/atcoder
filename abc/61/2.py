N,M = map(int,input().split())

roads = [[] for _ in range(N)]

for _ in range(M):
    a,b = map(int,input().split())
    roads[a-1].append(1)
    roads[b-1].append(1)

for i in roads:
    print(sum(i))