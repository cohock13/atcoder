N = int(input())
CSF = []
for i in range(N-1):
    CSF.append(list(map(int,input().split())))

for i in range(N):
    if i == N-1:
        print(0)
    else:
        ans = CSF[i][1]
        for j in range(i,N-1):
            if ans < CSF[j][1]:
                ans = CSF[j][1]
            elif ans%CSF[j][2] != 0:
                ans += (CSF[j][2]-ans%CSF[j][2])
            ans += CSF[j][0]
        print(ans)
            

