S = input()
l = len(S)
ans = 0
for i in range(l+1):
    for j in range(l-i):
        if int(S[j:i+j+1])%2019 == 0:
            ans += 1
print(ans)