from itertools import permutations

N = list(map(int,input().split()))
P = list(map(int,input().split()))

ans = []

for i in permutations(P):
    tmp = 1
    for j in range(3):
        tmp *= N[j]//i[j]
    ans.append(tmp)
    
print(max(ans))

        