N,K = map(int,input().split())
h = []
for i in range(N):
    h.append(int(input()))

h.sort()
tree = []

for i in range(N-K+1):
    tree.append(h[i+K-1]-h[i])

print(min(tree))