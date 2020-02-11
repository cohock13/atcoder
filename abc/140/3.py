N = int(input())
B = list(map(int,input().split()))

A = [0]*N

for i in reversed(range(N)):
    if i == N-1 :
        A[i] = B[-1]
    elif i == 0:
        A[i] = B[0]
    else:
        A[i] = min(B[i],B[i-1])

print(sum(A))