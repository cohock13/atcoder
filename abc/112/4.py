import numpy as np

def factorization(N):
    a = []
    for i in range(1,int(np.sqrt(N))+1):
        if N%i == 0:
            a.append(i)
    for j in range(len(a)):
        a.append(N//a[j])
    a.sort(reverse=True)
    return a

N,M = map(int,input().split())
f = factorization(M)
for i in f:
    if i <= M/N:
        print(i)
        exit()

