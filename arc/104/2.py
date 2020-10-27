N,S = input().split()
N = int(N)

num = [[0,0,0,0]]

a = t = g = c = 0


for i in S:
    if i == "A":
        a += 1
    elif i == "T":
        t += 1
    elif i == "G":
        g += 1
    else:
        c += 1
    num.append([a,t,g,c])

ans = 0
for i in range(N):
    for j in range(i+1,N+1):
        aa = num[j][0] - num[i][0] 
        tt = num[j][1] - num[i][1] 
        gg = num[j][2] - num[i][2] 
        cc = num[j][3] - num[i][3]

        if aa == tt and gg == cc:
            ans += 1

print(ans)  