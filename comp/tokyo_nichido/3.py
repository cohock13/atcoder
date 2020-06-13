"""
https://atcoder.jp/contests/tokiomarine2020/submissions/14229099
"""
N,K = map(int,input().split())
A = list(map(int,input().split()))

def update(A):
    b = [0]*N

    for i,a in enumerate(A):
        l = max(0,i-a)
        r = min(N-1,i+a)

        b[l] += 1
        if r+1 < N:
            b[r+1] -= 1
    
    res = []
    s = 0
    for i in b:
        s += i
        res.append(s)
    return res

for _ in range(min(K,75)):
    A = update(A)

print(*A)