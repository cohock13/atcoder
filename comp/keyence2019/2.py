N = int(input())

xl = []

for i in range(N):
    xl.append(list(map(int,input().split())))

itv = []

for i in range(N):
    right = xl[i][0] + xl[i][1]  ##right
    left = xl[i][0] - xl[i][1]  ##left   
    itv.append([right,left])
itv.sort()

ass = 0
tt = -1e10
for i in range(N):
    if tt <= itv[i][1]:
        ass += 1
        tt = itv[i][0]
print(ass)


            

