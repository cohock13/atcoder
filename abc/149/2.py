A,B,K = map(int,input().split())

if A-K>=0:
    print(A-K,end=" ")
    print(B)
elif A-K<0 and A+B-K>=0:
    print("0",end=" ")
    print(B-(K-A))
else:
    print("0 0")