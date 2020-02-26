N = int(input())
S = list(input())

we = []
west = 0
east = 0
for i in range(N):
    if S[i] == "W":
        west += 1
    elif S[i] == "E":
        east += 1
    we.append([west,east])

ans = 1e9
for i in range(N):
    if i == 0:
        left = 0
    else:
        left = we[i][0]
    right = we[N-1][1] - we[i][1]
    ans = min(ans,left+right)

print(ans)
