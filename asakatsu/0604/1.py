def is_the_day(m,d):
    return d >= 22 and (d%10) >= 2 and (d//10) >= 2 and (d%10)*(d//10) == m

M,D = map(int,input().split())

ans = 0

for m in range(1,M+1):
    for d in range(1,D+1):
        ans += int(is_the_day(m,d))

print(ans)