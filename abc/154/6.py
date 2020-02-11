r1,c1,r2,c2 = map(int,input().split())
from operator import mul
from functools import reduce

mod = int(1e9+7)

def comb(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

def path(C,R):
    return (C+2)*(comb(C+R+2,R)-R-1)/(R+1)

f = path(r2+1,c2+1)
g = path(r2+1,c1)
h = path(r1,c2+1)
r = path(r1,c1)

print((f+h-g-r)%mod)

    