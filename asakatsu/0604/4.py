from collections import Counter

N = int(input())
S = input()
mod = int(1e9+7)
c = Counter(S)

ans = 1

for i in c.values():
    ans *= (i+1)
    ans %= mod

print(ans-1)


