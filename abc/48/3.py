N,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0

for i in range(N-1):
    s = a[i] + a[i+1]

    if s <= x:
        continue
    else:
        a[i+1] = max(0,a[i+1]-(s-x))
        ans += s-x

print(ans)
