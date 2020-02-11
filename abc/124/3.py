S = list(input())
 
for i in range(len(S)):
    S[i] = int(S[i])
 
f = S[0]
ans = 0
 
for i in range(1,len(S)):
    if S[i]+S[i-1] != 1:
        ans += 1
        S[i] = int(not S[i])
 
print(ans)
        