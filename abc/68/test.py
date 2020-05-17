A = list(map(int,input().split()))

cnt = 0
for i in range(100000):
    if max(A) <= len(A) -1 :
        print(cnt)
        break
    else:
        ind = A.index(max(A))
        A[ind] -= len(A)
        cnt += 1
        for j in range(len(A)):
            if j != ind:
                A[j] += 1
