import math

N,H = map(int,input().split())
a = []
b = []

for i in range(N):
    A,B = map(int,input().split())
    a.append(A)
    b.append(B)

b.sort()
m = max(a)
ind = -1
for i in range(N):
    if b[i] > m:
        ind = i
        break

if ind == -1:
    print(math.ceil(H/m))
else:
    count = 0
    for i in reversed(range(ind,N)):
        if H > 0:
            H -= b[i]
            count += 1
        else:
            break
    if H > 0:
        count += math.ceil(H/m)
    print(count)