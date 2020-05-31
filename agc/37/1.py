S = input()

ans = 0
f = ""
i = 0
for _ in range(len(S)-1):
    print(i,ans,f)
    if S[i] == f:
        f = S[i] + S[i+1]
        i += 1
    else:
        f = S[i]
    ans += 1
    i += 1

print(ans)

