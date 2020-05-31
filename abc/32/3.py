N,K = map(int,input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
    exit()

ans = 0
l,r = 0,0
f = 1

for l in range(N):

    while r < N and f*s[r] <= K:##順序?
        f *= s[r]
        r += 1
    ans = max(ans,r-l)

    if r == l:
        r += 1
    else:
        f //= s[l]
    
print(ans)
