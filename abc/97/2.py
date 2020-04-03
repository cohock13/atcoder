import numpy as np

N = int(input())

expo = []
for i in range(1,10000):
    if i == 1:
        expo.append(i)
    else:
        for j in range(2,1000):
            tmp = i**j
            if tmp > N:
                break
            expo.append(tmp)
expo.sort()

expo = np.array(expo)

print(max(expo[expo<=N]))