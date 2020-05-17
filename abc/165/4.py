import math

def factor(N):
    ans = []
    for i in range(1,int(math.sqrt(N))+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    return ans

A,B,N = map(int,input().split())


print(min(N,B-1)*A//B)


"""
b = factor(B-1)
bb = factor(B)
a = factor(A)
aa = factor(A-1)
ans = -1e9
for i in b:
    if i <= N:
        ans = max(ans,math.floor(A*i/B)-A*math.floor(i/B))
for i in bb:
    if i <= N:
        ans = max(ans,math.floor(A*i/B)-A*math.floor(i/B))
for i in a:
    if i <= N:
        ans = max(ans,math.floor(A*i/B)-A*math.floor(i/B))
for i in aa:
    if i <= N:
        ans = max(ans,math.floor(A*i/B)-A*math.floor(i/B))
for i in range(int(math.sqrt(B))+2):
    ans = max(ans,math.floor(i*A/B)-A*math.floor(i/B))

print(ans)
"""