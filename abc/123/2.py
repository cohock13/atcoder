import numpy as np

N = []

for i in range(5):
    N.append(int(input()))

f = []

for i in range(5):
    f.append([N[i]%10,i])

f.sort()
m = 0

for i in range(5):
    if f[i][0] > 0:
        m = f[i][1]
        break

ans = 0

for i in range(5):
    if i == m:
        ans += N[i]
    else:
        ans += int(10*np.ceil(N[i]/10))   
 
print(ans)


##15m


