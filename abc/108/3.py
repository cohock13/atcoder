N,K = map(int,input().split())

a = 0
b = 0

tmp = K/2
for i in range(1,N+1):
    if i%K == 0:
        a += 1
    if i%K == tmp:
        b += 1
print(a**3 + b**3)