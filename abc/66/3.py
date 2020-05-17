from collections import deque
n = int(input())
a = list(map(int,input().split()))

ans = deque()

for i in range(n):
    if (n-i-1)%2 == 0:
        ans.appendleft(a[i])
    else:
        ans.append(a[i])

print(*ans)