##https://www.codechef.com/viewsolution/20131475

from math import gcd

def main():
    n = int(input())
    A = list(map(int , input().split()))
    N = 10**6+1

    sv = [i for i in range(10**6+1)]
    for i in range(2 ,int(N**0.5)+1) :
        if sv[i] < i : continue
        for j in range(i * i , N , i) :
            sv[j] = min(sv[j] , i)

    def getPrimes(a) :
        pr = []
        if a == 1 : return pr
        pr.append(sv[a])
        while a > 1 :
            if sv[a] != pr[-1] :
                pr.append(sv[a])
            a //= sv[a]
        return pr

    np = [0] * N
    F = [0] * N


    for a in A :
        pr = getPrimes(a)
        for i in range(1 << len(pr)) :
            prod , nb = 1 , 0
            for j in range(len(pr)) :
                if i & (1<<j) :
                    prod *= pr[j]
                    nb += 1
            F[prod] += 1
            np[prod] = nb

    ans = 0
    for i in range(N) :
        cnt = F[i]
        cnt = (cnt * (cnt-1))//2
        if np[i] & 1 : ans -= cnt
        else : ans += cnt

    if ans == (n*(n-1))//2:
        print("pairwise coprime")
        exit()

    A.sort()
    d = A[0]

    for i in A:
        d = gcd(i,d)
        if d == 1 or d > 10**2:
            break

    if d == 1:
        print("setwise coprime")
    else:
        print("not coprime")

main()
