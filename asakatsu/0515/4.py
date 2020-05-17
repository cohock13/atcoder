import numpy as np

def factor(N):
    ans = []
    for i in range(1,int(np.sqrt(N))+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    return ans

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a, b):
    return (a * b)//gcd(a,b)

N,M = map(int,input().split())
p = factor(M)

p.sort()

for i in reversed(range(len(p))):
    if p[i] <= M/N:
        print(p[i])
        break