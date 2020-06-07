N,Y = map(int,input().split())

for i in range(N+1):
    for j in range(N+1):
            m = Y - (10000*i+j*5000)
            if m >= 0 and (i+j+m//1000) == N:
                print(i,j,m//1000)
                exit()
print(-1,-1,-1)