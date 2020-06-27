from bisect import bisect
from collections import deque

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

csumA = [0]
csumB = [0]

s = 0
for i in A:
    s += i
    csumA.append(s)
s = 0
for i in B:
    s += i
    csumB.append(s)

ans = 0
for i in range(N+1):
    if K - csumA[i] >= 0:
        ##print(i,i+bisect(csumB,max(0,K-csumA[i])))
        ans = max(ans,i-1+bisect(csumB,max(0,K-csumA[i])))

for i in range(M+1):
    if K - csumB[i] >= 0:
        ans = max(ans,i-1+bisect(csumA,max(0,K-csumB[i])))

print(ans)
    
