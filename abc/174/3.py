K = int(input())

tmp = 7
for i in range(K):
    if tmp%K == 0:
        print(i+1)
        exit()
    tmp = (tmp*10+7)%K

print(-1)