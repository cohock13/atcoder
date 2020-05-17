from collections import Counter
from math import ceil

N,M = map(int,input().split())
name = input()
kit = input()


for i in name:
    if i not in kit:
        print("-1")
        exit()

n = Counter(name)
k = Counter(kit)

ans = 0
for i,j in zip(n.keys(),n.values()):
    ans = max(ans,ceil(j/k[i]))

print(ans)


