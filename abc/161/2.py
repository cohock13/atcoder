N,M = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
S = sum(A)
for i in A:
    if i >= S/(4*M):
        cnt += 1

if cnt >= M:
    print("Yes")
else:
    print("No")
