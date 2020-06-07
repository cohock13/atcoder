x = int(input())

n = (x//11)

x -= n*11
r = 0
if 0 < x <= 6:
    r = 1
elif 6 < x < 11:
    r = 2

print(2*n+r)