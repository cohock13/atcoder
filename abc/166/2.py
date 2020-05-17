N,K = map(int,input().split())
snuke = [0]*N
for i in range(K):
    d = int(input())
    A = list(map(int,input().split()))

    for j in A:
        snuke[j-1] += 1
cnt = 0
for i in snuke:
    if i == 0:
        cnt += 1

print(cnt)