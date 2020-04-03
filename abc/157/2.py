A = [-1]*101
d = []
for i in range(3):
    a,b,c = map(int,input().split())
    d.append(a)
    d.append(b)
    d.append(c)
    A[a] = 0
    A[b] = 0
    A[c] = 0
N = int(input())
b = []
for i in range(N):
    b.append(int(input()))

for i in range(N):
    A[b[i]] += 1

if (A[d[0]]==1 and A[d[1]]==1 and A[d[2]]==1) or (A[d[3]]==1 and A[d[4]]==1 and A[d[5]]==1) or (A[d[6]]==1 and A[d[7]]==1 and A[d[8]]==1) or (A[d[0]]==1 and A[d[3]]==1 and A[d[6]]==1) or (A[d[1]]==1 and A[d[4]]==1 and A[d[7]]==1) or (A[d[2]]==1 and A[d[5]]==1 and A[d[8]]==1) or (A[d[0]]==1 and A[d[4]]==1 and A[d[8]]==1) or (A[d[2]]==1 and A[d[4]]==1 and A[d[6]]==1):
    print("Yes")
else:
    print("No")