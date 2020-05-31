###どうして...

def check(c):
    tmp = []
    for i in range(N):
        tmp.append(w[i]*(p[i]-c))
    tmp.sort(reverse=True)
    ##濃度を実現するような食塩の取り方があるか
    if sum(tmp[:K]) < 0:
        return False
    else:
        return True

N,K = map(int,input().split())

r = 100
l = 0
eps = 10**(-10)
w = []
p = []

for _ in range(N):
    a,b = map(int,input().split())
    w.append(a)
    p.append(b)
    
while abs(r-l) > eps:
    mid = (r+l)/2
    if check(mid):
        l = mid
    else:
        r = mid

print(r)