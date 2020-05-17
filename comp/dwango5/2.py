N,K = map(int,input().split())
a = list(map(int,input().split()))

beauty = [[0]*len(a)]*len(a)

for i in range(len(a)):
    for j in range(i,len(a)):
        beauty[i][j] = sum(a[i:i+j+1])
        print(beauty[i][j],end=" ")
    
    print("\n")
        
        
for i in range(len(a)):
    for j in range(len(a)):
        print(beauty[i][j],end=" ")
    
    print("\n")

