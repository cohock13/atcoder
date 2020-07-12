res = [0]*10001

for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x

            if tmp <= 10000:
                res[tmp] += 1

N = int(input())

for i in range(1,N+1):
    print(res[i])
