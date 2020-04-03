S = input()
Q = int(input())
Atama = []
Osiri = []
rev = [0]*Q
for i in range(Q):
    a = list(input().split())
    if len(a) == 1:##T_i=1
        rev[i] = 1
    else:#T_i == 2
        if a[1] == "1":
            Atama.append([i,a[2],1])
        else:
            Osiri.append([i,a[2],-1])

##revの累積和
Rev = []
tmp = 0
r = sum(rev)
for i in range(len(rev)):
    r -= rev[i]
    Rev.append(r)
##print(Rev)
for i in range(len(Atama)):
    Atama[i][2] *= (-1)**Rev[Atama[i][0]]
for i in range(len(Osiri)):
    Osiri[i][2] *= (-1)**Rev[Osiri[i][0]]

Ans = Atama+Osiri
Ans.sort()
##print(Ans)
fw = ""
aw = ""
N = len(Ans)
for i in range(N):
    if Ans[i][2] == 1:
        fw += Ans[i][1]
    else:
        aw += Ans[i][1]

if sum(rev)%2 == 1:
    S = S[::-1]
fw = fw[::-1]

print(fw+S+aw)


