from itertools import combinations_with_replacement

N,M,Q = map(int,input().split())

comb = list(combinations_with_replacement(range(1,M+1),N))

abcd = []
for i in range(Q):
    a,b,c,d = map(int,input().split())
    abcd.append([a-1,b-1,c,d])

ans = 0
for i in comb:
    tmp = 0
    for a,b,c,d in abcd:
        if i[b] - i[a] == c:
            tmp += d
    ans = max(ans,tmp)

print(ans)








