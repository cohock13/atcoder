Q,H,S,D = map(int,input().split())
N = int(input())

a = (N//2)*D + (N%2)*min(4*Q,2*H,S)
b = N*S
c = H*2*N
d = Q*4*N

print(min(a,b,c,d))