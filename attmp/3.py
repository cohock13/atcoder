import itertools
a = list(map(int,input().split()))
S = sum(a)
num = [i for i in range(S)]
num += [-1 for j in range(max(0,9-S))]
ans = 0
for way in itertools.permutations(num,9):
    flag = True
    #yoko
    for i in range(0,7,3):
        for j in range(2):
            if way[i+j] > way[i+j+1]:
                flag = False
    ##tate
    for i in range(2):
        for j in range(0,7,3):
            if way[i+j] > way[i+j+1]:
                flag = False

    if flag:
        ans += 1

print(ans)        