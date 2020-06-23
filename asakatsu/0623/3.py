S = input()
K = int(input())
if len(set(S)) == 1:
    print(K*len(S)//2)
    exit()

cnt = 1
l,r = 1,1
T = S[::-1]
for i in range(l):
    if S[i] == S[i+1]:
        l += 1
    else:
        break

for i in range(l):
    if T[i] == T[i+1]:
        r += 1
    else:
        break

for i in range(l,len(S)-r):
    if S[i] == S[i+1]:
        cnt += 1
print(l,r,cnt)
print(K*(r//2+l//2+cnt//2))    