N,M = map(int,input().split())
##1からきている&&Nに行ける

road = [0]*N

for _ in range(M):
    a,b = map(int,input().split())

    if a == 1:
        road[b-1] += 1
    elif b == N:
        road[a-1] += 1

if 2 in road:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
