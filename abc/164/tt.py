P = 2019
S = input()
N = len(S)
res = 0
 
if P in [2,5]:
    for i in range(N):
        if int(S[i])% P == 0:
            res += i+1
else:
    dic = {0:1}
    t1 = 0
    t2 = 1
    for i in range(N):
        t2 = (10*t2) % P
        t1 = (int(S[N-1-i])*t2 + t1) % P
        if t1 in dic:
            res += dic[t1]
            dic[t1] += 1
        else:
            dic[t1] = 1
 
print(res)