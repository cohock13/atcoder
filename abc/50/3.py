from collections import Counter,defaultdict

N = int(input())
A = list(map(int,input().split()))
c = Counter(A)

if N%2 == 0:
    a = defaultdict(int)
    for i,j in zip(c.keys(),c.values()):
        a[i] = j
    
    for i in range(N//2):
        if a[i*2+1] != 2:
            print(0)
            exit()
    
    print(pow(2,N//2,int(1e9+7)))

else:
    a = defaultdict(int)
    for i,j in zip(c.keys(),c.values()):
        a[i] = j

    for i in range(N//2+1):
        if i == 0:
            if a[i] != 1:
                print(0)
                exit()
        else:
            if a[2*i] != 2:
                print(0)
                exit()

    print(pow(2,N//2,int(1e9+7)))
    

