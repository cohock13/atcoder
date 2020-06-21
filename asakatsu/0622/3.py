N = int(input())
a = list(map(int,input().split()))

s = sum(a)

if s%N != 0:
    print(-1)
else:
    m = [0]*N
    tmp = s//N

    for i in range(N):
        m[i] = a[i] - tmp
    
    s = 0
    ans = 0
    for i in range(N):
        s += m[i]
        if s != 0:
            ans += 1
    print(ans)