R,G,B,N = map(int,input().split())
c = sorted([R,G,B])
R = c[1]
G = c[2]
B = c[0]
ans = 0
for r in range(N//R+1):
    tmp = N - r*R
    for g in range(N//G+1):
        ttmp = tmp - g*G
        ans += (ttmp%B == 0 and ttmp >= 0)
print(ans)