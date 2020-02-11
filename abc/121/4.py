def F(N):
    if N%2 == 0:
        if N%4 == 0:
            return 0^N
        else:
            return 1^N
    else:
        if (N+1)%4 == 0:
            return 0
        else:
            return 1

A,B = map(int,input().split())

print(F(A-1)^F(B))


