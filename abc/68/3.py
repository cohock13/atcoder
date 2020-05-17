N,M = map(int,input().split())

goto_N = [0]*N
from_1 = [0]*N

for _ in range(M):
    a,b = map(int,input().split())
    if a == 1:
        from_1[b] = 1
    elif b == N:
        goto_N[a] = 1

for i in range(N):
    if goto_N[i] and from_1[i]:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")