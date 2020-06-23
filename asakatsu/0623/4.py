X = input()

ans = len(X)
tmp_s = 0
for i in X:
    if i == "S":
        tmp_s += 1
    else:
        if tmp_s > 0:
            ans -= 2
            tmp_s -= 1

print(ans)