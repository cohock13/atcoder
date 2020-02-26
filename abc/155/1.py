A = list(map(int,input().split()))
A.sort()

if (A[0] == A[1] and A[1] != A[2]) or (A[1] == A[2] and  A[0] != A[1]):
    print("Yes")
else:
    print("No")
