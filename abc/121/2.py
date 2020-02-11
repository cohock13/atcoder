N,M,C = map(int,input().split())
B = list(map(int,input().split()))

A = []
ans = 0
S = 0

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        S += tmp[j]*B[j]
    S += C

    if S>0:
        ans += 1
    
    S = 0

print(ans)

#5m