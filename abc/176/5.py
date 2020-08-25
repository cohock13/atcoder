from collections import defaultdict

H,W,M = map(int,input().split())
hw = defaultdict(int)

h = [0]*H
w = [0]*W

for _ in range(M):
    hh,ww = map(int,input().split())
    h[hh-1] += 1
    w[ww-1] += 1
    hw[(hh-1,ww-1)] = 1

def returnMaxs(a):
    m = max(a)
    ind = []
    for i in range(len(a)):
        if a[i] == m:
            ind.append(i)
    return ind

ind_h = returnMaxs(h)
ind_w = returnMaxs(w)

m = h[ind_h[0]]+w[ind_w[0]]

if len(ind_h)*len(ind_w) > M:
    print(m)
else:
    flag = False
    for i in ind_h:
        for j in ind_w:
            if hw[(i,j)] == 0:
                flag = True
    
    if flag:
        print(m)
    else:
        print(m-1)

