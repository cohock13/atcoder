import numpy as np
c = np.log(2)*2/3
def derivative(t):
    return 1 - c*P*np.exp(-c*t)

P = float(input())

if derivative(0) >= 0:
    print(P)
    exit()
"""
if derivative(P) <= 0:
    print(P+P*pow(2,-P/1.5))
"""
"""
r = P
l = 0
esp = 10**-12

while abs(r-l) > esp:
    mid = (r+l)/2

    if derivative(mid) > 0:
        r = mid
    else:
        l = mid
"""
l = np.log(c*P)/c
print(l+P*pow(2,-l/1.5))

