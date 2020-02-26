N = int(input())
X = list(map(int,input().split()))

dist = 0
ans = 1e6

for i in range(101):
    p = i
    dist = 0
    for j in range(N):
        dist += (X[j]-p)**2
    ans = min(ans,dist)

print(ans)

