from scipy.sparse.csgraph import shortest_path
import sys
import numpy as np
def input():
    return sys.stdin.readline().strip()
 
N = int(input())
 
graph = [[0 for i in range(N)] for j in range(N)]
 
for i in range(N-1):
    a,b,c = map(int,input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

Q,K = map(int,input().split())
dist = shortest_path(np.array(graph),indices=K-1)

for i in range(Q):
    x,y = map(int,input().split())
    print(int(dist[x-1]+dist[y-1]))
