import numpy as np
N,M,V,P = map(int,input().split())

A = list(map(int,input().split()))

A.sort() ##O(N)
B = []

for i in range(N):##O(N)
    if i<V:
        B.append(A[i]+M)
    else:
        B.append(A[i])
m = max(A)
tmp = np.array(B)
ANS = tmp[tmp>=m]
print(*ANS)
print(len(ANS))





