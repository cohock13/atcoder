from math import cos,sin,pi,sqrt
A,B,H,M = map(int,input().split())
m = 60*H + M
x = [A*cos(2*pi*m/(12*60)),B*cos(2*pi*m/60)]
y = [A*sin(2*pi*m/(12*60)),B*sin(2*pi*m/60)]
##print(x,y)
print(sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2))

