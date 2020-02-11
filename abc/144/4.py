import math

a,b,x = map(int,input().split())

if (a**2)*b>=2*x:
    ans = math.degrees(math.atan((a*(b**2)/(2*x))))
else:
    ans = math.degrees(math.atan(2*((a**2)*b-x)/a**3))

print(ans)