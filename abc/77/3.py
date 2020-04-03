import bisect

N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))

Upper = []
for i in B:##上の台について二分探索
    middle = bisect.bisect(A,i-1)
    Upper.append(middle)
for i in range(N-1):##累積和
    Upper[i+1] += Upper[i]
Upper = [0] + Upper

ans = 0
for i in C:
    bottom = bisect.bisect(B,i-1)
    ans += Upper[bottom]

print(ans)
