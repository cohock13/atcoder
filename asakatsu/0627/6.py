ans = 0

for _ in range(int(input())):
    a,b = map(int,input().split())
    ans += abs(a-b)

print(ans)