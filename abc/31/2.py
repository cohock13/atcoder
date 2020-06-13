L,H = map(int,input().split())
N = int(input())
A = [int(input()) for _ in range(N)]


for t in A:
    if t < L:
        print(L-t)
    elif L <= t <= H:
        print(0)
    else:
        print(-1)
