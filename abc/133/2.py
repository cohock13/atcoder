def main():
    import numpy as np 
    N,D = map(int,input().split())
    X = []
    
    for i in range(N):
        X.append(list(map(int,input().split())))
    
    ans = 0

    for i in range(N):
        for j in range(i+1,N):
            tmp = 0
            for h in range(D):
                tmp += (X[i][h]-X[j][h])**2
            dist = np.sqrt(tmp)
            if dist%1 == 0:
                ans += 1
    
    print(ans)


if __name__=="__main__":
    main()