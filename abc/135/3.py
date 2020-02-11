def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    ans = 0
    for i in reversed(range(N+1)):
        if i == N:
            ans += min(B[i-1],A[i])
            B[i-1] = max(0,B[i-1]-A[i])
        elif i == 0:
            ans += min(A[i],B[i])
        else:
            ans += min(B[i],A[i])
            A[i] = max(0,A[i]-B[i])
            ans += min(B[i-1],A[i])
            B[i-1] = max(0,B[i-1]-A[i])
        ##print(*A)
        ##print(*B)


    print(ans)


if __name__=="__main__":
    main()