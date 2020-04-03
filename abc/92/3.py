from copy import deepcopy
N = int(input())
A = list(map(int,input().split()))
A = [0] + A + [0]
dist = []
for i in range(N+1):
    dist.append(abs(A[i]-A[i+1]))
S = sum(dist)
for i in range(1,N+1):
    print(S+abs(A[i+1]-A[i-1])-abs(A[i]-A[i+1])-abs(A[i-1]-A[i]))

