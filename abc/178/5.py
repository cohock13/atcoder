N = int(input())

plus = []
minus = []
for _ in range(N):
    x,y = map(int,input().split())
    plus.append(x+y)
    minus.append(x-y)

ans1 = max(plus) - min(plus)
ans2 = max(minus) - min(minus) 

print(max(ans1,ans2))