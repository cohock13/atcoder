import numpy as np
def factor(N):
    ans = []
    for i in range(1,int(np.sqrt(N))+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    return ans

def check(K,N):
    while N >= K:
        if N%K == 0:
            N //= K
        else:
            N %= K
    if N%K == 1:
        return True
    else:
        return False

N = int(input())
ans = len(factor(N-1))-1

for K in factor(N)[1:]:
    if check(K,N):
        ans += 1

print(ans)            

