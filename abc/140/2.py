N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = 0

for i in range(N):
    if i == 0:
        ans += B[A[i]-1]
    else:
        if A[i] - A[i-1] == 1:
            ans += B[A[i]-1] + C[A[i]-2]
        else:
            ans += B[A[i]-1]

print(ans)
