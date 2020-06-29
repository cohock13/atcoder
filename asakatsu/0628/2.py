N = int(input())

t_0 = 0
x_0 = 0
y_0 = 0
flag = True

for _ in range(N):
    t,x,y = map(int,input().split())

    if not (abs(x-x_0) + abs(y-y_0) <= abs(t-t_0) and (abs(x-x_0)+abs(y-y_0))%2 == abs(t-t_0)%2):
        flag = False
    x_0 = x
    y_0 = y
    t_0 = t

print("Yes" if flag else "No")