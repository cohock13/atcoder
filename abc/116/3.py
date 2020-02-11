N = int(input())
h = list(map(int,input().split()))

ans = 0

for i in range(N-1):
    dist = h[i+1] - h[i]

    if dist > 0:
        ans += dist

print(ans+h[0])


