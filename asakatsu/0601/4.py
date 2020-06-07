def lunlun(K,S):
    if len(S) >= K:
        S.sort()
        print(S[K-1])
        return

    for a in range(len(S)):
        i = S[a]
        rem = i%10
        n = 10*i + rem

        if rem == 9:
            S.append(n)
            S.append(n-1)
        elif rem == 0:
            S.append(n)
            S.append(n+1)
        else:
            S.append(n)
            S.append(n+1)
            S.append(n-1)
    lunlun(K,S)


K = int(input())
S = [i for i in range(1,10)]

lunlun(K,S)