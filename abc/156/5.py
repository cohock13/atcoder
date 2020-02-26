def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

n,k = map(int,input().split())

if k>=n-1:
    ans = combination(2*n-1,n)
else:
    a = k+1
    ans = combination(2*a-1,a)

print(ans)