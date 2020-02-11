"""
O(N^2)
"""

N = int(input())
W = list(map(int,input().split()))

ans = 1e9

for i in range(N):
    f = sum(W[:i])
    l = sum(W[i:])
    ans = min(ans,abs(f-l))

print(ans)
    
#7m
