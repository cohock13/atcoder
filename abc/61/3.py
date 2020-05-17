N,K = map(int,input().split())
n = [0]*(int(1e5)+1)

for i in range(N):
    a,b = map(int,input().split())
    n[a] += b

for i in range(int(1e5)+1):
    K -= n[i]
    if K <= 0:
        print(i)
        break