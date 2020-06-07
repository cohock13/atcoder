N,K = map(int,input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
    exit()

if K == 0:
    print(0)
    exit()

from math import log10
from decimal import Decimal
log = [Decimal(log10(i)) for i in s]
K = Decimal(log10(K))

def check(l,r):
    return K >= log[r] - log[l]

for i in range(1,N):
    log[i] += log[i-1]

ans = 0

for i in range(N):

    r = N-1
    l = i

    for _ in range(5):
        mid = (r+l)//2 + 1
        if check(l,r):
            r = min((mid+r)//2,N-1)
        else:
            r = min((mid+l)//2,N-1)
        print(i,r)
    ans = max(ans,r-l)


print(ans)