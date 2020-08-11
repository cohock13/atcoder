from math import log
from decimal import Decimal

N,K = map(int,input().split())
A = list(map(int,input().split()))

B = [Decimal(log(i)) for i in A]

f = sum(B[:K])
for i in range(K,N):
    if f < (f-B[i-K]+B[i]):
        print("Yes")
    else:
        print("No")
    f = f-B[i-K]+B[i]

