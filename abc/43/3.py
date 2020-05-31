N = int(input())
a = list(map(int,input().split()))


ans = 1e10
for i in range(-100,101):
    tmp = 0
    for j in a:
        tmp += (i-j)**2
    ans = min(ans,tmp)

print(ans)