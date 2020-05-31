N = int(input())
a = [int(input()) for _ in range(N)]

c = {}
i = 0
for n in sorted(list(set(a))):
    c[n] = i
    i += 1

for i in a:
    print(c[i])