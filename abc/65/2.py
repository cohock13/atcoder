N = int(input())
a = [int(input()) for _ in range(N)]

tmp = a[0]-1
for i in range(N):

    if tmp == 1:
        print(i+1)
        exit()
    tmp = a[tmp]-1

print(-1)