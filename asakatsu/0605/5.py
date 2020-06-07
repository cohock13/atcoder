N_,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
mod = int(1e9+7)
if N_ == 1 or N_ == 2:
    print(0)
    exit()

"""
https://www.planeta.tokyo/entry/5195/
"""
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9+7
N = 10**5+1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans = 0
for i in range(N_):
    ans += cmb(i,K-1,mod)*A[i]

for j in range(N_):
    ans -= cmb(N_-j-1,K-1,mod)*A[j]

print(ans%mod)
