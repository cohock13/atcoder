N,K = map(int,input().split())
p = list(map(int,input().split()))
 
for i in range(N):
    p[i] = (p[i]+1)/2
a = [0]*(N-K+1)
f = sum(p[:K])
a[0] = f

for i in range(N-K):
    f = f + p[i+K] - p[i]
    a[i+1] = f
print(a)

print(max(a))