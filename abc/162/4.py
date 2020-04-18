N = int(input())
S = input()
R = S.count("R")
G = S.count("G")
ans = R*G*(N-R-G)

for i in range(N-2):
    for j in range(i,N-1):
        k = 2*j - i
        if k < N:
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1

            
print(ans)