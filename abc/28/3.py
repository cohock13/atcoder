from itertools import combinations

N = list(map(int,input().split()))

s = []
for i in combinations(N,r=3):
    s.append(sum(i))

s.sort()
print(s[-3])

