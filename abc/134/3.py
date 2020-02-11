def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    
    max_A = max(A)
    B = sorted(A)
    max2_A = B[N-2]

    if max_A == max2_A:
        for i in range(N):
            print(max_A)
        exit()
    
    for i in range(N):
        tmp=A[i]
        if tmp == max_A:
            print(max2_A)
        else:
            print(max_A)

if __name__=="__main__":
    main()