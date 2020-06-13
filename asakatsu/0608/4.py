n = int(input())
a = list(map(int,input().split()))

m = max(a)
res = 1e10
ans = 0
for i in a:
    if i != m:
        if abs(m//2-i) < res:
            res = abs(m//2-i)
            ans = i

print(m,ans)