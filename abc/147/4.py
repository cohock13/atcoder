import numpy as np 

N = int(input())
A = list(map(int,input().split()))

A = np.array(A,np.int64)##Ai<2^60

ans = 0
mod = int(1e9+7)

for i in range(60+1):
    bottom_bit = (A>>i)&1 ##i回シフトしたときの最下位bit
    ones = np.sum(bottom_bit[bottom_bit>0])##sum()だとTLE
    ##ans += (N-ones)*ones*(2**i) ##0の個数*1の個数*2^i個
    tmp = ones*(N-ones)
    for j in range(i):
        tmp = (tmp * 2) % mod ##爆発するのでfor文して毎回mod
    ans += tmp ##ここでオーバーフローはしないのだろうか?

print(ans%mod)