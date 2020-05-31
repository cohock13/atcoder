N,Q = map(int,input().split())

a = [0]*(N+1)
for _ in range(Q):
    l,r = map(int,input().split())
    a[l-1] += 1
    a[r] -= 1

for i in range(1,N):
    a[i] += a[i-1]

for i in range(N):
    print(a[i]%2,end="")
print()