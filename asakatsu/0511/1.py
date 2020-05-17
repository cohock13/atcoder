N,K = map(int,input().split())
t = [int(input()) for _ in range(N)]

for i in range(1,N-2):
    if t[i-1] + t[i] + t[i+1] < K:
        print(i+2)
        exit()

print(-1)
