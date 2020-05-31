N = int(input())
a = list(map(int,input().split()))

tmp,ans = 0,N


for i in range(1,N):
    if a[i] > a[i-1]:
        tmp += 1
    else:
        ans += tmp*(tmp+1)//2
        tmp = 0

ans += tmp*(tmp+1)//2
print(ans)