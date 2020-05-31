S = input()
T = int(input())

up = S.count("U")
down = S.count("D")
left = S.count("L")
right = S.count("R")
rem = S.count("?")
x = abs(left-right)
y = abs(up-down)

if T == 1:
    print(x+y+rem)
else:
    if x+y < rem:
        print((rem-x-y)%2)
    else:
        print(x+y-rem)
