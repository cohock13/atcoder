from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

"""nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]
"""
N = int(input())
l = list(map(int,input().split()))
R = 0
G = 0
B = 0
can = True
for i in range(len(l)):
    
    if l[i] == R:
        R+=1
    elif l[i] == G:
        G+=1
    else:
        B+=1

w = 1000000007
ans = (cmb(N,R)*cmb(N-R,G))%w

if (B == 0):
    ans *= 3
if(can):
    print(ans)
else:
    print(0)