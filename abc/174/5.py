from math import ceil

def BinarySearch(x):
    ans = sum([ceil(a/x)-1 for a in A])
    if ans <= K:
        return True
    else:
        return False

N,K = map(int,input().split())
A = list(map(int,input().split()))

r = max(A)
l = 0
eps = 10**-5

while abs(r-l) > eps:

    m = (r+l)/2

    if BinarySearch(m):
        r = m
    else:
        l = m

print(ceil(r)) 



