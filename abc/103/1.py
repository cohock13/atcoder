a = list(map(int,input().split()))
a.sort()

ans = 0
for i in range(len(a)-1):
    ans += abs(a[i]-a[i+1])

print(ans)