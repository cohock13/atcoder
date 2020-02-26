def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

N,X = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
dist = []

if X == 1:
    print(abs(x[0]-X))
    exit()

tmp = []
for i in range(N):
    tmp.append(abs(x[i]-X))
mindist = min(tmp)
for i in range(N-1):
    dist.append(abs(x[i]-x[i+1]))

ans = mindist

for i in range(N-1):
    ans = gcd(ans,dist[i])

print(ans)
