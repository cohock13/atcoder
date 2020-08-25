import sys
sys.setrecursionlimit(10**6)

N = int(input())

subord = [[] for _ in range(N)]

for i in range(N-1):
    n = int(input())
    subord[n-1].append(i+1)

def bfs(i):
    if len(subord[i]) == 0:
        return 1

    tmp = []
    for n in subord[i]:
        tmp.append(bfs(n))

    return max(tmp)+min(tmp)+1

a = bfs(0)
print(a)