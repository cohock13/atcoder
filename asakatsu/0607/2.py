N,A,B = map(int,input().split())


if (A-B)%2 == 0:
    print(abs(A-B)//2)
else:
    a = abs(A+B-1)//2 ##壁にぶつからない 
    b = abs(2*N-A-B+1)//2 ##壁にぶつかる
 
    print(min(a,b))


