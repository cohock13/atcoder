from math import ceil

N,C,K = map(int,input().split())
T = sorted([int(input()) for _ in range(N)])

d_t = T[0]
p = 1
ans = 1

for t in T[1:]:
    if p < C and t-d_t <= K:
        p += 1
    else:
        ans += 1
        d_t = t
        p = 1

print(ans)