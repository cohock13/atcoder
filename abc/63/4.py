import sys
import numpy as np
from math import ceil
"""
def input():
    return sys.stdin.readline().strip()
"""
def check(k):
    tmp = H - B*k
    
    
    flag = False
    for i in tmp:
        if i > 0:
            flag = True
            break
    if not flag:
        return True

    lf = 0
    for i in tmp:
        if i > 0:
            lf += ceil(i/(A-B))

    if lf <= k:
        return True
    else:
        return False

N,A,B = map(int,input().split())
h = np.array(list(int(input()) for _ in range(N)))

left = -1
right = 1e9

while abs(left-right) > 1:

    mid = (left+right)//2
    if check(mid):
        right = mid
    else:
        left = mid

print(int(right))
