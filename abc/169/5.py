N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N%2 == 1:
    print(B[N//2]-A[N//2]+1)
else:
    r = (B[N//2-1]+B[N//2])
    l = (A[N//2-1]+A[N//2])
    print(r-l+1)

    


    


    