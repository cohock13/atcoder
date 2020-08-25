N = int(input())
R = sorted(list(int(input()) for _ in range(N)),reverse=True)
pi = 3.1415926535

rad = 0
for i in range(N):
    if i%2:
        rad -= R[i]**2
    else:
        rad += R[i]**2

print(rad*pi)

