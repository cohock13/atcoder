import math
A,B,N = map(int,input().split())

ans = -1e10
for i in range(int(math.sqrt(B))+2):
    print(i)
    ans = max(ans,math.floor(i*A/B)-A*math.floor(i/B))

print(ans)