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

N = int(input())

if N <= 2:
    print(N)
    exit()
else:
    num = defaultdict(int)
    for i in range(2,N+1):
        for n,m in prime_factorize(i):
            num[n] += m


ans = 1
mod = int(1e9+7)
for i in num.values():
    ans = ((i+1)*ans)%mod

print(ans) 