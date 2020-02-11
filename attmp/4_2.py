import numpy as np 
import sys

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a, b):
    return (a * b)//gcd(a,b)

N,M = map(int,input().split())
a = list(map(int,input().split()))

A = np.array(a)

while np.sum(A%2) == 0:
    A = A//2

if np.sum(A%2) != len(A):
    print("0")
    sys.exit()
    
tmp = 1##LCM

for i in range(N):
    tmp = lcm(tmp,a[i]//2)

if tmp > M:
    print("0")

else:
    print((M//tmp+1)//2)

