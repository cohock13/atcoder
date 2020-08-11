N = int(input())
A = list(int(input()) for _ in range(N))
A.sort()

if N%2:
    print(2*(sum(A[N//2+1:])-sum(A[:N//2]))-A[0])
else:
    print(2*(sum(A[N//2:])-sum(A[:N//2]))-A[0])

