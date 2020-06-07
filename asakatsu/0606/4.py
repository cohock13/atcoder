from itertools import combinations_with_replacement
N,M,Q = map(int,input().split())

abcd = [tuple(map(int,input().split())) for _ in range(Q)]

ans = 0
for n in combinations_with_replacement(range(1,M+1),N):
    tmp = 0
    for a,b,c,d in abcd:
        if n[b-1] - n[a-1] == c:
            tmp += d
    
    ans = max(ans,tmp)


print(ans)