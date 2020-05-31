from math import ceil
x = int(input())

m = x//11
r = x%11

if 0 < r <= 6:
    print(2*m+1)
elif r == 0:
    print(2*m)
else:
    print(2*m+2)