def res(n):
    pos = n
    cnt = 1
    while 1:
        pos = P[pos]-1
        if pos == n:
            break
        cnt += 1

    tmp = 0
    ans = -float("inf")
    pos = n

    for _ in range(min(K,cnt)):
        pos = P[pos]-1
        tmp += C[pos]
        ans = max(ans,tmp)
    
    ##ループして0以上なら(K//cnt)回ループしてあまりをシミュレーション
    if tmp > 0 and K > cnt:
        pos = n
        d = K%cnt
        tmp = (K//cnt-1)*tmp
        ans = max(ans,tmp)
        for _ in range(d+cnt):
            pos = P[pos]-1
            tmp += C[pos]
            ans = max(ans,tmp)

    return ans

N,K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = -float("inf")
for i in range(N):
    ans = max(ans,res(i))

print(ans)

