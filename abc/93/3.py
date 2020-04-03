A = list(map(int,input().split()))
A.sort()
B = []
for i in A:
    B.append(i%2)

ans = 0

if B.count(1) == 1:
    for i in range(3):
        if B[i] == 0:
            A[i] += 1
    ans += 1
elif B.count(0) == 1:
    for i in range(3):
        if B[i] == 1:
            A[i] += 1
    ans += 1

ans += A[2] - A[1]
A[0] += A[2] - A[1]
ans += (A[2]-A[0])//2

print(ans)
