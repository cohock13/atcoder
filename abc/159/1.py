def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

N,M = map(int,input().split())
a = 0
b = 0
if N <= 1:
    a = 0
else:
    a = combination(N,2)
if M <= 1:
    b = 0
else:
    b =  combination(M,2)
print(a+b)