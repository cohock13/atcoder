N = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(N):
    if p[i] == i+1:
        try:
            p[i+1],p[i] = p[i],p[i+1]
        except:
            pass
        ans += 1

print(ans) 