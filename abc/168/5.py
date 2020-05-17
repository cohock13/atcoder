from bisect import bisect,bisect_left

N = int(input())
AB = [tuple(map(int,input().split())) for _ in range(N)]

plus = []
minus = []

for A,B in AB:

    if A == 0 or B == 0:
        plus.append(0)
        minus.append(0)
    else:
        plus.append(A/B)
        minus.append(-B/A)

plus.sort()
minus.sort()

dame = [0]*N

for i,p in enumerate(plus):
    l = bisect_left(minus,p)
    r = bisect_left(minus,p)

    if minus[l] == p and 

print(dame)


mod = int(1e9)+7

ans = pow(2,N,mod) - 1

non = 0
for d in dame:
    if d > 0:
        non += (pow(2,d,mod)-2)*pow(2,N-d-2,mod) + pow(2,N-3,mod)##だめなやつ,かぶりなし
        non %= mod
print(ans,non//2)
print(ans-non//2)
