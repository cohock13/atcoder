N,M = map(int,input().split())

s = []
for i in range(M):
    s.append(list(map(int,input().split())))

p = list(map(int,input().split()))


ans = 0

for i in range(2**N):
    for j in range(M):
        tmp = 0
        for h in range(s[j][0]):
            if (i>>(s[j][h]-1))&1 == 1:
                tmp += 1
        if tmp%2 !=p[j]:
            break
        else:
            ans += 1

print(ans)

