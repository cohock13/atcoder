def runrun(K,S):
    if K <= len(S):
        S.sort()
        ##print(S)
        print(S[K-1])
        return 
    else:
        for i in range(len(S)):
            tmp = S[i]%10
            if tmp == 9:
                S.append(S[i]*10+8)
                S.append(S[i]*10+9)
            elif tmp == 0:
                S.append(S[i]*10+1)
                S.append(S[i]*10)
            else:
                S.append(S[i]*10+tmp-1)
                S.append(S[i]*10+tmp)
                S.append(S[i]*10+tmp+1)
        S = list(set(S))
        runrun(K,S)

if __name__ == "__main__":
    K = int(input())
    S = []
    for i in range(1,10):
        S.append(i)
    runrun(K,S)




