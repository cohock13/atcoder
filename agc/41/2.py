def check(n):

    if n <= P-1:
        return True

    if A[n]+M < A[P-1]:
        return False
    
    votes = (P+N-1-n)*M + sum([A[n]+M-i for i in A[P-1:n]])

    if votes < M*V:
        return False
    else:
        return True

N,M,V,P = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)

##開区間
right = N
left = 0

while abs(right-left) > 1:

    mid = (right+left)//2

    if check(mid):
        left = mid
    else:
        right = mid

print(left+1)






