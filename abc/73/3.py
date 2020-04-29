N = int(input())
A = {}

for i in range(N):
    a = int(input())
    if a in A:
        A[a] ^= 1
    else:
        A[a] = 1

print(sum(A.values()))