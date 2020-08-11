N = int(input())
A = list(map(int,input().split()))

l = []
s = 0
for i in range(N-1):
    if A[i] > A[i+1]:
        l.append([s,i])
        s = i+1
    else:
        continue

l.append([s,N-1])

ans = 1000
for s,e in l:
    kabu = (ans//A[s])
    ans += (A[e]-A[s])*kabu
    ##print(ans,kabu)

print(ans)
