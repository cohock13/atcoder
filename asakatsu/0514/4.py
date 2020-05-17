N = int(input())
num = [[0 for _ in range(10)] for j in range(10)]
for i in range(1,N+1):
    s = str(i)
    f = int(s[0])
    l = int(s[-1])
    if l == 0:
        continue
    num[f][l] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            tmp = num[i][j]*num[j][i]
            ans += 2*tmp
        else:
            tmp = num[i][j]*num[j][i]
            ans += 2*tmp

print(ans//2)
