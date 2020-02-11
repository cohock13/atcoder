import numpy as np 

N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    if i>=K:
        p = 0
    else:
        p = np.ceil(np.log2(K/i))
    ans += (0.5**p)/N

print(ans)
