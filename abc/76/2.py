N = int(input())
K = int(input())
tmp = [2**(i+1)-2**i for i in range(10)]
t = 1
for i in range(N):
    if 2**i < K:
        t *= 2
    else:
        t += K
print(t)