from itertools import combinations
n = int(input())
b = list(map(int,input().split()))
r = b[0]
b = b[1:]
print("0:")
ans = []
for i in range(1,r+1):
    for j in combinations(b,i):
        comb = list(j)
        comb.reverse()
        s = 0
        for h in comb:
            s += 2**h
        ans.append([s,list(j)])

ans.sort()

for i,j in ans:
    print(str(i)+":",*j)

