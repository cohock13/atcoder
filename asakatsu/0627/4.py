N = int(input())
A = list(map(int,input().split()))
mod = 10**9+7

cnd = []
if N%2 == 0:
    for i in range(N//2):
        cnd.append(2*i+1)
        cnd.append(2*i+1)
else:
    for i in range(N//2+1):
        if i == 0:
            cnd.append(0)
        else:
            cnd.append(2*i)
            cnd.append(2*i)
            
B = sorted(A)
if cnd != B:
    print(0)
    exit()

print(pow(2,N//2,mod))
