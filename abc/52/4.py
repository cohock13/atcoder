N,A,B = map(int,input().split())
x = list(map(int,input().split()))
ans = 0
for i in range(N-1):
    ans += min(B,A*(x[i+1]-x[i]))

print(ans)