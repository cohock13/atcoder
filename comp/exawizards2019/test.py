N = int(input())
S = {}
for i in range(N):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1

key = list(S.keys())
value = list(S.values())
m = max(value)

Ans = []
for i in range(len(key)):
    Ans.append([value[i],key[i]])
Ans.sort()
for i in range(len(key)):
    if Ans[i][0] == m:
        print(Ans[i][1])
    