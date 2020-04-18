n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

flag = [0]*2000
for j in range(2**n):
    tmp = 0
    for h in range(n):
        if (j>>h)&1:
            tmp += A[h]
    flag[tmp] = 1

for i in m:
    if flag[i]:
        print("yes")
    else:
        print("no")