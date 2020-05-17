X,Y = map(int,input().split())

tmp = X
ans = [X]
for i in range(int(1e5)):
    tmp *= 2
    if tmp > Y:
        break
    ans.append(tmp)

print(len(ans))
