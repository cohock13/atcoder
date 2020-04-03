n = int(input())
a = list(map(int,input().split()))
a.sort()
M = max(a)
m = M/2
tmp = 1e9
for i in range(n-1):
    if tmp > abs(a[i]-m):
        tmp = abs(a[i]-m)
        ans = i

print(M,a[ans])