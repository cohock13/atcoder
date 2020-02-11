N,Q = map(int,input().split())
S = (input())

lr = []

for i in range(Q):
    lr.append(list(map(int,input().split())))

acs = [0]*(N+1)
tmp = 0
for i in range(N-1):
    if S[i] =="A" and S[i+1] =="C":
        tmp = 1
    else:
        tmp = 0
    acs[i+1] = acs[i] + tmp
    

for i in range(Q):
    print(acs[lr[i][1]-1]-acs[lr[i][0]-1])
