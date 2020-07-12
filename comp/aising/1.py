L,R,d = map(int,input().split())
ans = 0
for i in range(L,R+1):
    ans += int(i%d == 0)

print(ans)