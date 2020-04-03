S = list(input())
T = list(input())

ans = "No"
for i in range(len(S)+1):
    tmp = S.pop(0)
    S.append(tmp)
    ##print(S)
    if S == T:
        ans = "Yes"
        break

print(ans)