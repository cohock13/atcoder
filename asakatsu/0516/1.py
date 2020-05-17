N,K = map(int,input().split())

snukes = [1]*N

for _ in range(K):
    d = int(input())
    A = list(map(int,input().split()))

    for i in A:
        snukes[i-1] = 0

print(sum(snukes))