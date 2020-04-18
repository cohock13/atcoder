from itertools import combinations

n,k = map(int,input().split())

num = [i for i in range(n)]
ans = []
for i in combinations(num,k):
    comb = list(i)
    comb.reverse()

    s = 0
    for j in comb:
        s += 2**j
    ans.append([s,list(i)])

ans.sort()
for i,j in ans:
    print(str(i)+":",*j)
