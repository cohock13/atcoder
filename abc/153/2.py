H,N = map(int,input().split())
A = list(map(int,input().split()))

s = sum(A)

if H>sum(A):
    print("No")
else:
    print("Yes")