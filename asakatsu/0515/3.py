from math import ceil

N,K = map(int,input().split())
A = list(map(int,input().split()))

if K >= N:
    print(1)
else:
    print(ceil((N-1)/(K-1)))