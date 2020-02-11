import itertools

N = int(input())
PER = []
for i in range(N):
    PER.append(i+1)

P = list(map(int,input().split()))
Q = list(map(int,input().split()))
a = 0
b = 0
tmp = 1

for x in itertools.permutations(PER):
     
    flag_a = 0
    flag_b = 0
 
    for i in range(N):
        if x[i] == P[i]:
            flag_a += 1   
        if x[i] == Q[i]:
            flag_b += 1
    if flag_b == N:
        b = tmp
    if flag_a == N:
        a = tmp
    tmp += 1

ans = a - b
if ans < 0:
    ans = - ans

print(ans)
        
    
