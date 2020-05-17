from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

r = defaultdict(int)
l = defaultdict(int)

for i,a in enumerate(A):
    r[i-a] += 1
    l[i+a] += 1

ans = 0
for i in r.keys():
    ans += r[i]*l[i]

print(ans)  



