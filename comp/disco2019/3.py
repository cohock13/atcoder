H,W,K = map(int,input().split())
cake = []
ls = []
zeroh = [0]*H
for i in range(H):
    c = input()
    tmp = c.rfind("#")
    if tmp == -1:
        zeroh[i] = 1
        tmp = W-1
    ls.append(tmp)
    cake.append(list(c))
ans = []
num = 1
split = [0]*W
for i in range(H):
    if zeroh[i]:
        ans.append(split)
    if not zeroh[i]:
        split = []
        for j in range(W):
            split.append(num)
            if cake[i][j] == "#" and j<ls[i]:
                num += 1
        num += 1
        ans.append(split)

notzeropoint = 0
for i in range(H):
    if ans[i][0] != 0:
        notzeropoint = i
        break

for i in range(notzeropoint):
    for j in range(W):
        ans[i][j] = ans[notzeropoint][j]


for i in range(H):
    print(*ans[i])