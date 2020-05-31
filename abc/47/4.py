N,T = map(int,input().split())
A = list(map(int,input().split()))
v = []

m = A[0]
for i in A:
    m = min(i,m)
    v.append(i-m)

print(v.count(max(v)))

