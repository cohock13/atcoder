N = int(input())
A = list(int(input()) for _ in range(N))

a = A[0]

for i in A[1:N-1]:
    a ^= i

if a != A[-1]:
    print(-1)
    exit()

a = 0
ans = [0]

for i in A[:N-1]:
    a ^= i
    ans.append(a)

print(*ans,sep="\n")