N,M = map(int,input().split())
w = list(map(int,input().split()))
lv = []
for _ in range(M):
    tmp = tuple(map(int,input().split()))
    lv.append(tmp)

def able():
    m = 1e10

    for _,i in lv:
        m = min(i,m)
    
    if m > min(w):
        return False
    return True

##だめ
if not able():
    print(-1)
    exit()

m = 0
for i,_ in lv:
    m = max(i,m)

##二部探索？
l = 0
r = 2*max(m)*(N-1)

while abs(l-r) < 1:
    m = (l+r)//2

    if check(m):
        r = m
    else:
        l = m

print(r,l,m)