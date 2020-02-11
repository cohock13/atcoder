import numpy as np 

H,N = map(int,input().split())

A,B = np.array([list(map(int,input().split())) for i in range(N)]).T

dp = np.zeros(H+1,dtype=np.int32)

for i in range(1,H+1):
    dp[i] = np.amin(dp[np.maximum(i-A,0)]+B)
    
print(dp[H])


    



