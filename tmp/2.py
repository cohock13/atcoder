N = int(input())
S,T = input().split()

ans = ""
for i in range(2*N):
    if i%2 == 0:
        ans += S[i//2]
    else:
        ans += T[i//2]

print(ans)