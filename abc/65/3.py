def fact(n):
    res = 1
    for i in range(2,n+1):
        res = (res*i)%1000000007
    return res

N,M = map(int,input().split())

if abs(N-M) >= 2:
    print(0)
elif N == M:
    print(2*fact(N)*fact(M)%1000000007)
else:
    print(fact(N)*fact(M)%1000000007)