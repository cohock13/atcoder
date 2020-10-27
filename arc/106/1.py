N = int(input())

five = 5
f = 1
while five <= N:

    tmp = N - five
    three = 0
    while tmp:
        if tmp%3 != 0:
            break
        tmp //= 3
        three += 1
    
    if tmp == 1 and three > 0:
        print(three,f)
        exit()
    
    five *= 5
    f += 1

print(-1)

        