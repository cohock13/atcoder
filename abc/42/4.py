def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

H,W,A,B = map(int,input().split())

if H == A or W == B:
    print(0)
    exit()

mod = int(1e9)+7
S = combination(H+W-2,min(H-1,W-1))
M = combination(H-1,B-1)
B = (-A+B-W+1)*combination(A-B+W-2,A-1)//(B-W)
A = (B+1)*combination(A+B,A-1)//A - 1
A = (A%mod)*(B%mod)*(M%mod)
print(S,A,B,M)
print((S-A)%mod)

