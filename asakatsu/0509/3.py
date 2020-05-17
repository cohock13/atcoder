N,K = map(int,input().split())

ans = 0
m = 0
ab = []
for i in range(N):
    ab.append(list(map(int,input().split())))

ab.sort()

tmp = 0
for a,b in ab:
    tmp += b
    if tmp >= K:
        print(a)
        break