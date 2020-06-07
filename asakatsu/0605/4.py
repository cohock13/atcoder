import numpy as np

N = int(input())
A = np.array(list(map(int,input().split())))

ans = 0
mod = int(1e9+7)

for i in range(61):
    tmp = np.sum((A>>i)&1)
    p = (N-tmp)*tmp
    for j in range(i):
        p = (p*2)%mod
    ans += p
print(ans%mod)