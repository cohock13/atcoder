from math import ceil
def combination(n,r,mod=10**9+7):
    if r > n:
        return 0

    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

N,K = map(int,input().split())

m = int(ceil(N/2))
mod = int(1e9+7)
for i in range(1,K+1):
    """
    if i > m:
        print(0)
        continue
    """

    print(combination(K-1,i-1)*combination(N-K+1,i)%mod)



