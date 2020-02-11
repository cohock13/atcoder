N,K = map(int,input().split())
S = input()
ans = ""

for i in range(len(S)):
    if i+1 == K:
        ans += str.lower(S[i])
    else:
        ans += S[i]

print(ans)