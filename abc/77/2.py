import numpy as np
N = int(input())
sqs = np.array([],dtype="int64")
for i in range(1,31623):
    sqs = np.append(sqs,i**2)
print(max(sqs[sqs<=N]))
