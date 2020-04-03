N,M = map(int,input().split())
v = 100*(N-M) + 1900*M
p = (2**M-1)/(1-2**(-M))
print(int(v*p))