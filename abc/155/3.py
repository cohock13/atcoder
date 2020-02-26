N = int(input())
S = []

for i in range(N):
    tmp = input()
    S.append(tmp)
S.sort()
if N == 1:
    print(S[0])
    exit()
ans = []
SS = []
count = 1

for i in range(N-1):
    if i == N-2:
        if S[i] == S[i+1]:
            count += 1
            ans.append(count)
            SS.append(S[i])
        else:
            ans.append(count)
            SS.append(S[i])
            ans.append(1)
            SS.append(S[i+1])
    elif S[i] == S[i+1]:
        count += 1
    else:
        ans.append(count)
        SS.append(S[i])
        count = 1

m = max(ans)

for i in range(len(SS)):
    if ans[i] == m:
        print(SS[i])



    


