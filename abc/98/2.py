N = int(input())
S = list(input())

ans = 0

for i in range(1,N-1):
    left = set(S[:i])
    right = set(S[i:])
    ans = max(ans,len(list(left&right)))

print(ans)
