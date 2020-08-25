import numpy as np


N = int(input())
HS = list(tuple(map(int,input().split())) for _ in range(N))
HS = np.array(HS)
##実現できる高度を二部探索 O(NlogN)

def check(m):
    time = []
    for h,s in HS:
        time.append((m-h)//s)

    time.sort()
    for i in range(N):
        if time[i] < i:
            return False
    return True

l = 0
r = 1e12
eps = 1e-4

while abs(l-r) > eps:

    m = (r+l)/2

    if check(m):
        r = m
    else:
        l = m

print(int(r))