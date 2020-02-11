import math

def ceil(n,m):
    return int(math.ceil(n/m))

N = int(input())
A = []

for i in range(5):
    A.append(int(input()))


print(ceil(N,min(A))+4)
