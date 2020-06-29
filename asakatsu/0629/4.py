from collections import defaultdict

N = int(input())
a = list(int(input()) for _ in range(N))

b = sorted(list(set(a)))

d = defaultdict(int)
index = 0
for i in b:
    d[i] = index
    index += 1

for i in a:
    print(d[i])

