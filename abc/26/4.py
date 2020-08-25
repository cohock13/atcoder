from math import sin,pi

def check(m):
    return A*m+B*sin(C*m*pi) > 100

A,B,C = map(int,input().split())

l = 0
r = 1e10
eps = 10**-12

while abs(r-l) > eps:
    
    m = (r+l)/2

    if check(m):
        r = m
    else:
        l = m

print(r)

