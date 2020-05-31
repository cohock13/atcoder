from bisect import bisect

N,M = map(int,input().split())

edge = [[] for _ in range(N)] 

for _ in range(M):
    a,b,y = map(int,input().split())
    edge[a-1].append(y)
    edge[b-1].append(y)

for i in edge:
    i.sort(reverse=True)

print(edge)

for i in range(int(input())):
    v,w = map(int,input().split())
    print(bisect(edge[v-1],w)+1)


