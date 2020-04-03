D,N = map(int,input().split())

if D == 0:
    if N == 100:
        print(101)
    else:
        print(N)
elif D == 1:
    if N == 100:
        print(101*100)
    else:
        print(N*(100**D))
else:
    if N == 100:
        print(101*(100**D))
    else:
        print(N*(100**D))

    