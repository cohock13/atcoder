N = int(input())
A = list(map(int,input().split()))

ans = 100

for i in A:
    tmp = i
    cnt = 0
    while tmp%2 == 0 and tmp > 0:
        tmp //= 2
        cnt += 1
    ans = min(ans,cnt)

print(ans)