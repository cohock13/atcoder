N,K = map(int,input().split())
p = list(map(int,input().split()))

for i in range(N):
    p[i] = (p[i]+1)/2
for i in range(N-1):
    p[i+1] += p[i]

ans = []

for i in range(N-K+1):
    if i == 0:
        ans.append(p[K-1])
    else:
        ans.append(p[i+K-1]-p[i-1])
print(max(ans))




