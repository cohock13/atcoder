N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = 1
mod = 10**9+7
tmp_K = K
if min(A) > 0:
    A.sort(reverse=True)
    for i in A[:K]:
        ans = (ans*i)%mod
 
elif max(A) < 0:
    if K%2 == 0:
        A.sort()
        for i in A[:K]:
            ans = (ans*i)%mod
    else:
        A.sort(reverse=True)
        for i in A[:K]:
            ans = (ans*i)%mod
else:
    z = []
    p = []
    m = []
    for i in A:
        if i == 0:
            z.append([i,1])
        elif i > 0:
            p.append([i,1])
        else:
            m.append([i,1])
    m.sort()
    mm = []
    for i in range(0,len(m),2):
        try:
            mm.append([m[i][0]*m[i+1][0],2])
        except:
            pass
    
    tot = p+z+mm+m

    tot.sort(reverse=True)
    flag_m = False
    for v,cost in tot:
        if K <= 0:
            break
        if v < 0:
            flag_m = True
        if K - cost >= 0:
            ans = (ans*v)%mod
            K -= cost
        else:
            continue

    if flag_m and len(z) == 0:##値が負になる．絶対値の最小化を行う．
        b = sorted(list([[abs(i),i] for i in A]))
        bb = list(i for _,i in b)
        res = 1
        for i in range(tmp_K):
            res = (res*bb[i])%mod
        print(res%mod)
        exit()
print(ans%mod)