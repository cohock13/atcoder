from copy import deepcopy

N = int(input())
X = list(map(int,input().split()))
Y = deepcopy(X)
Y.sort()
med1 = Y[N//2-1]
med2 = Y[N//2]
##print("med1:",med1,"med2",med2)
for i in range(N):
    if X[i] > med1:
        print(med1)
    else:
        print(med2)
    