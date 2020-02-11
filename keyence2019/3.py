N,K,S = map(int,input().split())

ans = [0]*N

if S == 1e9:
    for i in range(K):
        ans[i] = S
    for i in range(K,N):
        ans[i] = 1 
else:
    for i in range(K):
        ans[i] = S
    for i in range(K,N):
        ans[i] = S+1
    

print(*ans)


    

