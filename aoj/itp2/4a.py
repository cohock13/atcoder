n = int(input())
a = list(map(int,input().split()))

q = int(input())

for i in range(q):
    b,e = map(int,input().split())
    tmp = a[b:e]
    tmp.reverse()
    a = a[:b] + tmp + a[e:]

print(*a)
