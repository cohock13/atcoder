N = int(input())
h = list(map(int,input().split()))

ans = h[0]

for i in range(N-1):
    ans += max(0,h[i+1]-h[i])
    
print(ans)