N = int(input())

s = [input() for _ in range(N)]

for i in range(N):
    tmp = ""
    for j in reversed(range(N)):
        tmp += s[j][i]
    print(tmp)
