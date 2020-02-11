"""
O(N)
"""

N = int(input())
W = list(map(int,input().split()))

ls = 0
rs = sum(W)
ans = 1e9

for i in range(N):
    ls += W[i]
    ans = min(ans,abs((rs-ls)-ls))

print(ans)