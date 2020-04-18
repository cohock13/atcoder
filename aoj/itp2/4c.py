from copy import deepcopy
n = int(input())
a = list(map(int,input().split()))

for i in range(int(input())):
    b,e,t = map(int,input().split())
    tmp = deepcopy(a)
    for k in range(e-b):
        a[t+k] = tmp[b+k]
        a[b+k] = tmp[t+k]

print(*a)