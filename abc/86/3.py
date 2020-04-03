N = int(input())
ans = "Yes"
x = 0
y = 0
t = 0
for i in range(N):
    t_i,x_i,y_i = map(int,input().split())
    x_i = abs(x_i-x)
    y_i = abs(y_i-x)
    t_i = abs(t_i-t)
    
    if x_i+y_i <= t_i and (x_i+y_i-t_i)%2 == 0:
        continue
    else:
        ans = "No"
    x = x_i
    y = y_i
    t = t_i

print(ans)
