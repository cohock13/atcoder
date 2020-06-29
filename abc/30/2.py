from numpy import angle,exp,pi

n,m = map(int,input().split())

a = exp(1j*(n%12+m/60)*2*pi/12)
b = exp(1j*m*2*pi/60)

ans = abs(angle(a,deg=True)-angle(b,deg=True))
print(min(ans,360-ans))