W,H,N = map(int,input().split())
x_r = W
x_l = 0
y_r = H
y_l = 0

for _ in range(N):
    x,y,a = map(int,input().split())
    if a == 1:
        x_l = max(x,x_l)
    elif a == 2:
        x_r = min(x,x_r)
    elif a == 3:
        y_l = max(y,y_l)
    else:
        y_r = min(y,y_r)


print(max(0,(x_r-x_l))*max(0,(y_r-y_l)))


