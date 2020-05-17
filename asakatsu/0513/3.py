from collections import defaultdict

def dfs(s):
    tmp = []
    if len(info[s]) == 0:
        return 1
    tmp = []
    for i in info[s]:
        tmp.append(dfs(i))
    return max(tmp)+min(tmp)+1

N = int(input())
info = [[] for _ in range(N)]

for i in range(N-1):
    b = int(input())
    info[b-1].append(i+1)

print(dfs(0))

