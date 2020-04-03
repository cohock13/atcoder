c = []
for i in range(3):
    c.append(list(map(int,input().split())))
ans = "Yes"
for i in range(3):
    for j in range(i+1,3):
        tmp = []
        for h in range(3):
            tmp.append(c[h][i]-c[h][j])
        if len(set(tmp)) != 1:
            ans = "No"
            break

print(ans)