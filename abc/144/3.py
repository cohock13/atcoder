import math
N = int(input())
ans = float("inf")

for i in range(1,int(math.sqrt(N))+1):
    if N%i == 0:
        ans = min(ans,i+N//i-2)
print(int(ans))
