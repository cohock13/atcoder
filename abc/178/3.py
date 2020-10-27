N = int(input())

mod = 10**9+7

niko = 0
zero = 1
kyu = 1
nai = 8


for _ in range(N-1):
    niko = niko*10 + (zero+kyu)
    zero = nai+zero*9
    kyu = nai+kyu*9
    nai *= 8
    
    niko %= mod
    zero %= mod
    kyu %= mod
    nai %= mod
    ##print(niko,zero,kyu,nai,niko+zero+kyu+nai)

print(niko)