from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
a = int(input())
b = int(input())
n = int(input())

m = lcm(a,b)
for i in range(100000):
    if m*i >= n:
        print(m*i)
        break
