N,M = map(int,input().split())

H = list(map(int,input().split()))
good = [1]*N

for i in range(M):
    a,b = map(int,input().split())

    if H[a-1] > H[b-1]:
        good[b-1] = 0
    elif H[a-1] < H[b-1]:
        good[a-1] = 0
    else:
        good[a-1] = 0
        good[b-1] = 0


print(sum(good))

