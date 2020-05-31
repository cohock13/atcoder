import sys
from collections import defaultdict

def input():
    return sys.stdin.readline().strip()

def recordnum(a,b):
    if not (0 < a < H-1 and 0 < b < W-1):
        return 

    res = M[(a,b)]
    for i,j in vector:
        res += M[(a+i,b+j)]
    num[res] += 1
    return

def dfs(a,b,color):

    if visited[(a,b)]:
        return

    recordnum(a,b)
    visited[(a,b)] = True

    if color == "b":
        for i,j in vector:
            x = a+i
            y = b+j
            if 0 < x < H-1 and 0 < y < W-1 and M[(x,y)] == 0:
                dfs(x,y,"w")
    return

    

H,W,N = map(int,input().split())

M = defaultdict(int)
visited = defaultdict(int)
ab = []

for _ in range(N):
    a,b = map(int,input().split())
    ab.append((a-1,b-1))
    M[(a-1,b-1)] = 1


vector = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
num = [0]*10

for a,b in ab:
    dfs(a,b,"b")

num[0] = (H-2)*(W-2) - sum(num)

for i in num:
    print(i)



