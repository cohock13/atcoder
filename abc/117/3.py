N,M = map(int,input().split())
X = list(map(int,input().split()))

X.sort()

if N >= M:
    print(0)
    exit()

distance = []

for i in range(M-1):
    distance.append(abs(X[i]-X[i+1]))

distance.sort()

print(sum(distance)-sum(distance[M-N:]))