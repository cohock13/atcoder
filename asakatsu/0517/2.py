N = int(input())

mod = int(1e9)+7

ans = 1
for i in range(1,N+1):
    ans = (ans*i)%mod


print(ans)