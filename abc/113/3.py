N,M = map(int,input().split())
py = []

for i in range(M):
    p,y = map(int,input().split())
    py.append([p,y,i])

py.sort()

P = [0]*(N+1)
ID = []

for p,y,i in py:
    
    P[p] += 1 ##どの県に何個市があるかカウント

    p_tmp = str(p)
    y_tmp = str(P[p])

    upper = "0"*max(0,6-len(p_tmp))+p_tmp
    lower = "0"*max(0,6-len(y_tmp))+y_tmp

    ID.append([i,upper+lower])

ID.sort()

for _,i in ID:
    print(i)
