from math import gcd
K = int(input())
s = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            s += gcd(a,gcd(b,c))

print(s)

