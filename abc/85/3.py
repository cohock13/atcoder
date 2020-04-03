N,Y = map(int,input().split())

for i in range(N+1):
    for j in range(N+1):
        sen = Y - i*10000 - j*5000
        if sen >= 0 and (sen//1000+i+j) == N:
            print(i,j,sen//1000)
            exit()

print(-1,-1,-1) 