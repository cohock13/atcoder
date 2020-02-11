N,K = map(int,input().split())
H = list(map(int,input().split()))

H.sort(reverse=True)

for i in range(N):
    if i<K:
        H[i] = 0


print(sum(H))