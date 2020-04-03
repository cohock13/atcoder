N = int(input())
a = list(map(int,input().split()))
ans = 0
tmp = 1
for i in range(N):
    if a[i] != tmp:
        ans += 1
    else:
        tmp += 1
if ans == N:
    print(-1)
else:
    print(ans)
    