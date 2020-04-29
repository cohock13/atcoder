def search(y,x):
    flag = True
    for i in range(y,y+R):
        for j in range(x,x+C):
            if F[i][j] != P[i-y][j-x]:
                flag = False
    return flag


H,W = map(int,input().split())
F = []
for i in range(H):
    F.append(list(input()))
R,C = map(int,input().split())
P = []
for i in range(R):
    P.append(list(input()))

for i in range(H-R+1):
    for j in range(W-C+1):
        if search(i,j):
            print(i,j)