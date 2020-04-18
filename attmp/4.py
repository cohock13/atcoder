import math

N,Q = map(int,input().split())
A = list(map(int,input().split()))
S = list(map(int,input().split()))
l = len(A)
for i in S:
    flag = True
    ans = i
    for j in range(l):
        ans = math.gcd(ans,A[j])
        if ans == 1:
            flag = False
            print(j+1)
            break
    if flag:
        print(ans)
