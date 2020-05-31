from collections import Counter
import sys
sys.setrecursionlimit(10**6)

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]

def dfs(i,s,no,total):
    global ans

    if i == l:

        if no != 0:
            if total/no == A:
                tmp = 1
                for i in range(l):
                    if s[i] > 0:
                        tmp *= cmb(num[i][1],s[i])
                ans = ans+tmp
        return
                
    for n in range(num[i][1]+1):
        dfs(i+1,s+[n],no+n,total+num[i][0]*n)


N,A = map(int,input().split())
x = list(map(int,input().split()))

num = list(zip(Counter(x).keys(),Counter(x).values()))


l = len(num)
ans = 0
dfs(0,[],0,0)

print(ans)

