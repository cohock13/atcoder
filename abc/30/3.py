from bisect import bisect_left
 
N,M = map(int,input().split())
X,Y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
##なるべく早い便を探す
time = a[0]
dep = 0
 
while 1:
    dep += 1
    if dep%2:##A to B
        tmp = bisect_left(b,time+X)
        if tmp == M:
            break
        time = b[tmp]
    else:#B to A
        tmp = bisect_left(a,time+Y)
        if tmp == N:
            break
        time = a[tmp]
 
print(dep//2)