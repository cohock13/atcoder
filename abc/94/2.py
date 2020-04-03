import numpy as np
N,M,X = map(int,input().split())
A = list(map(int,input().split()))
A = np.array(A)
print(min(len(A[A<X]),len(A[A>=X])))