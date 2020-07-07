from itertools import combinations
from collections import defaultdict
from copy import deepcopy
H,W,K = map(int,input().split())

M = list(list(input()) for _ in range(H))
way = defaultdict()
ans = 0

for i in range(H+1):
    for j in range(W+1):
        for x in combinations(range(0,H),i):
            for y in combinations(range(0,W),j):
                tmp = deepcopy(M)
                for s in x:
                    for a in range(W):
                        tmp[s][a] = "r"
                for t in y:
                    for a in range(H):
                        tmp[a][t] = "r"
                if sum(i.count("#") for i in tmp) == K:
                    ans += 1

print(ans)

                