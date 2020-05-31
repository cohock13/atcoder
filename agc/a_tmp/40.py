S = input()
N = len(S)+1
l = 0
r = 0

ll = [0]*N
rr = [0]*N
for i in S:
    if i == "<":
        l += 1
        r = 0
    else:
        r += 1
        l = 0
    lr.append((l,r))
print(lr)
ans = 0
for l,r in lr:
    ans += max(l,r)

print(ans)