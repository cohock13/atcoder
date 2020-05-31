def edit(L,R,T):
    for i in range(L-1,R):
        ans[i] = T

N,Q = map(int,input().split())
ans = [0]*N

for i in range(Q):
    L,R,T = map(int,input().split())
    edit(L,R,T)

for i in ans:
    print(i)