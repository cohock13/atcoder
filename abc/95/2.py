N,X = map(int,input().split())
m = []
for i in range(N):
    m.append(int(input()))

X -= sum(m)

print(N+X//min(m))
