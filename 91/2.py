N = int(input())
red = {}
for i in range(N):
    tmp = input()
    if tmp in red:
        red[tmp] += 1
    else:
        red[tmp] = 1

M = int(input())
for i in range(M):
    tmp = input()
    if tmp in red:
        red[tmp] -= 1

print(max(0,max(red.values())))

