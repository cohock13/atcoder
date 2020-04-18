from operator import itemgetter
N = int(input())
A = list(map(int,input().split()))
B = sorted(enumerate(A), key=itemgetter(1),reverse=True)
##print(B)
ans = 0
cnt = 0
flag = [1 for _ in range(N)]
for i,j in B:
    if flag[i]:
        ans += j
        if i < N-1:
            flag[i+1] = 0
        if i > 0:
            flag[i-1] = 0
        flag[i] = 0
        cnt += 1
    if cnt == N//2:
        break

print(ans)
    
        