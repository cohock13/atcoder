N = int(input())


dig = [[0 for _ in range(10)] for i in range(10)]

for i in range(1,N+1):
    n = str(i)
    f = int(n[0])
    l = int(n[-1])
    dig[f][l] += 1


ans = 0

for i in range(10):
    for j in range(10):
        ans += dig[i][j]*dig[j][i]

print(ans)
