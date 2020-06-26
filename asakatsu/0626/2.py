N = int(input())

txy = list(tuple(map(int,input().split())) for _ in range(N))

t_0 = 0
x_0 = 0
y_0 = 0

for t,x,y in txy:
    dt = t - t_0
    dx = x - x_0
    dy = y - y_0
    if (abs(dx) + abs(dy))%2 == dt%2 and (abs(dx)+abs(dy)) <= dt:
        t_0 = t
        x_0 = x
        y_0 = y
    else:
        print("No")
        exit()

print("Yes")