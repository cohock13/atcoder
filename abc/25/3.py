N,D,K = map(int,input().split())

LR = [tuple(map(int,input().split())) for _ in range(D)]
ST = [tuple(map(int,input().split())) for _ in range(K)]

for S,T in ST:
    pos = S
    day = 1
    if T > S:

        for L,R in LR:
            if L <= pos:
                pos = max(pos,R)
            if pos >= T:
                print(day)
                break
            day += 1

    else:
        for L,R in LR:
            if R >= pos:
                pos = min(pos,L)
            if pos <= T:
                print(day)
                break
            day += 1
