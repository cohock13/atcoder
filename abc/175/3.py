X,K,D = map(int,input().split())

X = abs(X)

if X-K*D <= 0:
    d = X//D
    if (K-d%2)%2:
        print(D-X%D)
    else:
        print(X%D)
else:
    print(X-K*D)
