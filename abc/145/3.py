import math

N = int(input())
D = []

for k in range(N):
    x,y = map(int,input().split())
    D.append([x,y])

ans = 0

for i in range(N):
    for j in range(N):
        ans += math.sqrt((D[i][0]-D[j][0])**2 +(D[i][1]-D[j][1])**2)

print(ans/N)
