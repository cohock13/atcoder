import bisect

n = int(input())
a = sorted(list(map(int,input().split())))
a.append(1e20)

for i in range(int(input())):
    k = int(input())
    place = bisect.bisect_left(a,k)
    print(1 if a[place] == k else 0)
