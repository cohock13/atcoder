import math

def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

X,Y = map(int,input().split())

ans = 0

if (X+Y)%3 == 0 and 2*Y-X>=0 and 2*X-Y>=0:
    up,right = (2*Y-X)//3,(2*X-Y)//3
    ans = combination(up+right,right)

print(ans)


