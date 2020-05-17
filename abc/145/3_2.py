from itertools import permutations
from numpy import sqrt
def dist(x,y):
    return sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

N = int(input())

d = [list(map(int,input().split())) for _ in range(N)]

ans = 0
l = 0
for way in permutations(range(0,N)):
    l += 1
    for i in range(N-1):
        ans += dist(d[way[i]],d[way[i+1]])
    
print(ans/l)