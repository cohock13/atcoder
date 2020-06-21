from collections import defaultdict

N = int(input())
A = list(map(int,input().split()))

d = defaultdict(int)

for i in A:
    d[i] += 1

Q = int(input())

res = sum(A)

for _ in range(Q):
    b,c = map(int,input().split())
    res -= b*d[b]
    res += c*d[b]
    d[c] += d[b]
    d[b] = 0

    print(res)