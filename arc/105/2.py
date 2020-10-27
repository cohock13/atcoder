from math import gcd

N = int(input())
a = list(map(int,input().split()))

m = min(a)

ans = m

for i in a:
    ans = gcd(ans,i)

print(ans)