N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)


tmp = A[:(N+1)//2]
if N%2 == 0:
    print(2*sum(tmp)-A[0])
else:
    print(2*sum(tmp)-A[0]-tmp[-1])


