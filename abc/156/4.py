def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

def power_func(a,n,p):
    bi=str(format(n,"b"))#2進表現に
    res=1
    for i in range(len(bi)):
        res=(res*res) %p
        if bi[i]=="1":
            res=(res*a) %p
    return res

mod = int(1e9+7)
n,a,b= map(int,input().split())

S = (power_func(2,n,mod) - 1)%mod
A = combination(n,a)
B = combination(n,b)
ans = (S-A-B)%mod

print(ans)