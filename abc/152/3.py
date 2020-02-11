N = int(input())
P = list(map(int,input().split()))

minp = P[0]
ans = 0

for i in range(N):
    minp = min(minp,P[i])
    if minp == P[i]:
        ans += 1

print(ans)


