H,W = map(int,input().split())

a = []

for _ in range(H):
    a.append(list(map(int,input().split())))

n_order = 0
order = []
for i in range(H):
    for j in range(W):
        if j != W-1:
            if a[i][j]%2 == 1:
                a[i][j+1] += 1
                a[i][j] -= 1
                n_order += 1
                order.append([i+1,j+1,i+1,j+2])
        else:
            if a[i][j]%2 == 1:
                try:
                    a[i][j] -= 1
                    a[i+1][j] += 1
                    n_order += 1
                    order.append([i+1,j+1,i+2,j+1])
                except:
                    pass

print(n_order)
for i in order:
    print(*i)
