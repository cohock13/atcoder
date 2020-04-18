import bisect

input()
a = list(map(int,input().split()))

for i in range(int(input())):
    k = int(input())
    print(bisect.bisect_left(a,k),bisect.bisect(a,k))