N = int(input())
S = {}
for i in range(N):
    tmp = input()
    if tmp not in S:
        S[tmp] = 0
    S[tmp] += 1

M = max(S.values())

L = list(S)
L.sort()
for i in L:
    if S[i] == M:
        print(i)

