from itertools import permutations
 
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
 
p = 0
q = 0
i = 0
for n in permutations(range(1,N+1)):
    if n == P:
        p = i
    if n == Q:
        q = i
    i += 1
 
print(abs(p-q))