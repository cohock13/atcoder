K,N = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
dist = []
for i in range(N-1):
    dist.append([A[i+1]-A[i],i])
dist.sort()
ind = dist[-1][1]
ans = min(A[-1]-A[0],A[ind]+abs(K-A[ind+1]))

print(ans)