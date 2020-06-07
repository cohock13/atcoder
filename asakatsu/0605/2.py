N = int(input())
A = sorted(list(map(int,input().split())))

t = 1

for i in A:
    t *= i

    if t > 10**18:
        print(-1)
        exit()

print(t)