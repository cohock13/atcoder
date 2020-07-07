N,M = map(int,input().split())

ac = [0]*N
p = [0]*N
ans = 0
for _ in range(M):
    a,b = input().split()
    a = int(a)-1

    if not ac[a]:
        if b == "AC":
            ac[a] = 1
            ans += p[a]
        else:
            p[a] += 1

print(sum(ac),ans)
