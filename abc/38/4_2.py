from bisect import bisect_left
def search(a,n):

    p = 0

    if n == 1:
        for i in range(10**5+1):
            if a[i]:
                
    
    else:


N = int(input())

W = [[] for _ in range(10**5+1)]
H = [[] for _ in range(10**5+1)]


for _ in range(N):
    w,h = map(int,input().split())
    W[w].append(h)
    H[h].append(w)

ans = 1
