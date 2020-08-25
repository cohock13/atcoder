def check(i,j,h):
    return i!=j and j!=h and h!=i and i+j>h and j+h>i and i+h>j

N = int(input())
L = list(map(int,input().split()))

ans = 0
for i in range(N):
    for j in range(i,N):
        for h in range(j,N):
            ans += check(L[i],L[j],L[h])

print(ans)


