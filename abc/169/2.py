N = int(input())
A = list(map(int,input().split()))

tmp = 1

if 0 in A:
    print(0)
    exit()

for i in A:
    tmp *= i
    if tmp > 10**18:
        print(-1)
        exit()


print(tmp)