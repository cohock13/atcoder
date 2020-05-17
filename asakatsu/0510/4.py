def saiki(n,A):

    if n == N:
        A.sort()
        for i in A:
            print(i)
        return

    alpha = list("abcdefghijklmnopqr")

    tmp = []

    for i in A:
        a = alpha.index(sorted(list(i))[-1])
        for j in range(a+2):
            tmp.append(i+alpha[j])
    
    saiki(n+1,tmp)

N = int(input())

saiki(1,["a"])