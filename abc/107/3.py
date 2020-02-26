N,K = map(int,input().split())
x = list(map(int,input().split()))

ans = 1e12
    
for i in range(N-K+1):
    a = abs(x[i])+abs(x[i]-x[i+K-1])
    b = abs(x[i+K-1]) + abs(x[i]-x[i+K-1])
    ans = min(ans,min(a,b))

print(ans)