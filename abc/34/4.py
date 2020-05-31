def salt(a,i):
    return a[i][0]*abs(a[i][1])*0.01

def water(a,i):
    return a[i][0] - salt(a,i)


N,K = map(int,input().split())

sw = []
for i in range(N):
    w,p = map(int,input().split())
    sw.append((w,p))

if K >= N:
    """
    容器の水全部取る
    """
    salt = 0
    water = 0

    for w,p in sw:
        salt += w*p*0.01
        water += w*(1-0.01*p)
    
    print(salt/(salt+water))

else:
    """
    濃度が一番高いものを選ぶ.そこから,(なるべく容積の少ない水を取る,なるべく濃度の高い水を取る)
    をシミュレートし,その中でのMaxがこたえ.
    """

    sw.sort(reverse=True,key=lambda x:x[1])
    m_water = sorted([(i,-j) for i,j in sw])
    ##print(sw,m_water)
    max_salt = sw[0][0]*sw[0][1]*0.01
    max_water = sw[0][0]*(1-sw[0][1]*0.01)


    ##[salt,water]
    max_sw = [[0,0] for _ in range(K)]
    min_sw = [[0,0] for _ in range(K)]
    ##濃度の高いものについての累積和
    for i in range(1,K):
        max_sw[i][0] = max_sw[i-1][0] + salt(sw,i)
        max_sw[i][1] = max_sw[i-1][1] + water(sw,i)
    ##容量の小さいものについて累積和
    for i in range(1,K):
        min_sw[i][0] = min_sw[i-1][0] + salt(m_water,i-1)
        min_sw[i][1] = min_sw[i-1][1] + water(m_water,i-1)
    ##答えの計算
    ans = 0
    for i in range(K):
        s = max_salt + max_sw[i][0] + min_sw[K-i-1][0]
        w = max_water + max_sw[i][1] + min_sw[K-i-1][1]
        ans = max(ans,s/(s+w)*100)
    print(ans)
        

