S = input()

c = 0
ans = [0]
for i in S:
    if i == "R":
        c += 1
    else:
        ans.append(c)
        c = 0
ans.append(c)
print(max(ans))