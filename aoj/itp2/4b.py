from collections import deque
from copy import deepcopy
n = int(input())
a = list(map(int,input().split()))
q = int(input())

for i in range(q):
    b,m,e = map(int,input().split())
    tmp = deepcopy(a)
    for k in range(e-b):
        a[b+(k+e-m)%(e-b)] = tmp[b+k]

print(*a)