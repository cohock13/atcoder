N,M = map(int,input().split())

if 2*N > M:
    print(M//2)
else:
    M -= 2*N
    print(N+M//4)