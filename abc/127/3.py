N,M = map(int,input().split())
R = [0]*M
L = [0]*M

for i in range(M):
    L[i],R[i] = map(int,input().split())

print(max(0,min(R)-max(L)+1))
