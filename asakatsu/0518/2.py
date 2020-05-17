N = int(input())
s = [int(input()) for _ in range(N)]

if sum(s)%10 != 0:
    print(sum(s))
    exit()

ans = 0

for i in s:
    tmp = sum(s) - i
    if tmp%10 != 0:
        ans = max(ans,tmp)

print(ans)