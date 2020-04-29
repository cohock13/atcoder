n = int(input())

graph = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    v = list(map(int,input().split()))
    for j in v[2:]:
        graph[v[0]-1][j-1] = 1

for i in graph:
    print(*i)