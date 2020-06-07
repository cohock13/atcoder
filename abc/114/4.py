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
factor = [0]*101

for i in range(1,N+1):
    f = prime_factorize(i)
    for p,n in f:
        factor[p] += n

ov2 = 0
ov4 = 0
ov14 = 0
ov24 = 0
ov74 = 0
for f in factor:
    if 2 <= f:
        ov2 += 1
    if 4 <= f:
        ov4 += 1
    if 14 <= f:
        ov14 += 1
    if 24 <= f:
        ov24 += 1
    if 74 <= f:
        ov74 += 1

ans = 0
##(2,4,4)
ans += (ov2-ov4)*(ov4)*(ov4-1)//2 + ov4*(ov4-1)*(ov4-2)//2

##(2,24)
ans += (ov2-ov24)*(ov24) + (ov24-1)*(ov24)

##(14,4)
ans += (ov4-ov14)*(ov14) + (ov14-1)*(ov14)

##(74)
ans += ov74

print(ans)