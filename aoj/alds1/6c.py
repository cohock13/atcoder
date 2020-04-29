from collections import deque

def partition(A,p,r):
    x = A[r]
    i = p-1

    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]

    return i+1

def quicksort(A,p,r):
    if p < r:
        q = partiton(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

n = int(input())

A = deque()
stable = deque()
for i in range(n):
    s,t = input().split()
    t = int(t)
    A.append([t,s])

print(A)
print(sorted(A))
A.sort()
print(A)