N = list(map(int,input().split()))

p = [i%2 for i in N]

ans = 0

if sum(p) == 0 or sum(p) == 3:
    m = max(N)
    for i in N:
        ans += (m-i)//2
elif sum(p) == 1:
    for i in range(3):
        if N[i]%2 == 0:
            N[i] += 1
    ans += 1
    m = max(N)
    for j in N:
        ans += (m-j)//2
else:
    for i in range(3):
        if N[i]%2 == 1:
            N[i] += 1
    ans += 1
    m = max(N)
    for j in N:
        ans += (m-j)//2

print(ans)
    