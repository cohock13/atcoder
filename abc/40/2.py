n = int(input())

ans = 1e20
for i in range(1000):
    for j in range(1000):
        if i*j <= n:
            ans = min(ans,abs(i-j)+(n-i*j))

print(ans)