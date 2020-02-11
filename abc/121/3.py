import numpy as np 

N,M = map(int,input().split())
AB = []
for i in range(N):
    a,b = map(int,input().split())
    AB.append([a,b])

need = M
cost = 0

AB.sort()

for i in range(N):
    if need - AB[i][1] >= 0:
        need -= AB[i][1]
        cost += AB[i][0]*AB[i][1]
    else:
        cost += AB[i][0]*need 
        break    

print(cost)


#12m
    


