from collections import defaultdict

N = int(input())
a = list(map(int,input().split()))

dic = defaultdict(int)
mi = 0

for i in a:
    dic[i] = 1
    while dic[mi]:
        mi += 1
    print(mi)


