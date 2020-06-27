def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9+7
n = 5*10**5+1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

rui = [1]
s = 1
for i in range(1,5*10**5+1):
    s *= i
    s %= p
    rui.append(s)

N,M = map(int,input().split())
mod = 10**9+7

res = 0
for i in range(max(0,2*N-M),N+1):
    print(i)
    res += cmb(N,i,mod)*(rui[i]*rui[i])*(rui[N-i]**2)
    res %= mod

print(res)
