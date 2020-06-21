N,Q = map(int,input().split())
lr = [0]*N

for _ in range(Q):
    l,r = map(int,input().split())
    lr[l-1] += 1
    if r < N:
        lr[r] -= 1

s = 0
csum = []
for i in lr:
    s += i
    csum.append(s)

ans = ""
for i in csum:
    ans += str(i%2)

print(ans)