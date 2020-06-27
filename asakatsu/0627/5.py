from collections import defaultdict

def prime_factorize(N): #素因数分解
    exponent = 0
    while N%2 == 0:
        exponent += 1
        N //= 2
    if exponent: factorization = [[2,exponent]]
    else: factorization = []
    i=1
    while i*i <=N:
        i += 2
        if N%i: continue
        exponent = 0
        while N%i == 0:
            exponent += 1
            N //= i
        factorization.append([i,exponent])
    if N!= 1: factorization.append([N,1])
    assert N != 0, "zero"
    return factorization

A,B = map(int,input().split())

f = defaultdict(int)


##(B,A-B]までの整数の積の素因数の数が分かればいい
for i in range(A-B):
    ff = prime_factorize(B+i+1)
    for p,n in ff:
        f[p] += n

mod = 10**9+7

ans = 1
for i in f.values():
    ans = (ans*(i+1))%mod

print(ans)