N = int(input())
S = input()

ans = 0

tmp = 0

for i in S:
    if i == "I":
        tmp += 1
    else:
        tmp -= 1
    ans = max(ans,tmp)

print(ans)