N = int(input())

A = [0 for i in range(N)]
X = [[0 for i in range(15)] for j in range(15)]
Y = [[0 for i in range(15)] for j in range(15)]

for i in range(N):
    A[i] = int(input())
    for j in range(A[i]):
        X[i][j],Y[i][j]= map(int,input().split())

ans = 0
for i in range(N):
    ##i番目が正直だとする
    if 


    

