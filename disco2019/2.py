N = int(input())
A = list(map(int,input().split()))
S = sum(A)/2
Es = []
tmp = 0
for i in range(N):
    tmp += A[i]
    Es.append(abs(tmp-S))
cut_point = Es.index(min(Es))

ans1 = abs(sum(A[cut_point:])-sum(A[:cut_point]))
ans2 = abs(sum(A[cut_point+1:])-sum(A[:cut_point+1]))
ans = min(ans1,ans2)

print(ans)