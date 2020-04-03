"""
https://atcoder.jp/contests/abc014/submissions/10397932
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
def dfs(v=0, p=-1, d=0):
    parent[0][v] = p
    depth[v] = d
    for u in T[v]:
        if u == p:
            continue
        dfs(u, v, d+1)
 
def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    while depth[v] > depth[u]:
        diff = depth[v] - depth[u]
        v = parent[diff.bit_length()-1][v]
    if u == v:
        return u
    for k in range(logN-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]
 
N = int(input())
logN = (N - 1).bit_length()
T = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    T[x-1].append(y-1)
    T[y-1].append(x-1)
 
parent = [[0] * N for _ in range(logN+1)]
depth = [0] * N
dfs()
for k in range(logN):
    for v in range(N):
        if parent[k][v] < 0:
            parent[k+1][v] = -1
        else:
            parent[k+1][v] = parent[k][parent[k][v]]

print(parent)