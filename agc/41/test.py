N,M,V,P = map(int,input().split())
A = list(map(int,input().split()))
 
#二分探索するからAをsortする
A = sorted(A,reverse=True)
 
left=0
right=N-1
 
while left<=right:
    mid = (left+right)//2
 
    if mid<P:#そもそも入っている
        left = mid + 1
    elif A[mid] + M < A[P-1]:
        right = mid -1
    else:
        voted = P * M
        for _ in range(mid+1,N):
            voted += M
 
        for v in A[P-1:mid]:
            voted += A[mid]+M-v
 
        if voted >= M*V:
            left= mid+1
        else:
            right = mid-1
 
print(left)