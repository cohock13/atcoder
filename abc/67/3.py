N = int(input())
a = list(map(int,input().split()))
csum = []
s = 0

for i in range(N):
    s += a[i]
    csum.append(s)

if N == 2:
    print(abs(a[0] - a[1]))
    exit()

s = sum(a)
ans = 1e10
for i in range(1,N-1):
    ans = min(ans,abs(2*csum[i]-s))

print(ans)