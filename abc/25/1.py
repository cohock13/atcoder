A,B,C,K = map(int,input().split())
S,T = map(int,input().split())

cost = A*S+T*B

if (S+T) >= K:
    cost -= C*(S+T)

cost = max(cost,0)

print(cost)