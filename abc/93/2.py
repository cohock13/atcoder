A,B,K = map(int,input().split())
ans = []
for i in range(A,min(A+K,B)):
    ans.append(i)
for j in range(max(A,B-K+1),B+1):
    ans.append(j)
ans = list(set(ans))
ans.sort()
for h in ans:
    print(h)