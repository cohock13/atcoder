

from bisect import bisect,bisect_left,insort
dic = {}
l = []
for i in range(int(input())):
    order = list(input().split())

    if order[0] == "0":
        if order[1] in dic:
            dic[order[1]] = int(order[2])
        else:
            dic[order[1]] = int(order[2])
            insort(l,order[1])
    elif order[0] == "1":
        if order[1] in dic:
            print(dic[order[1]])
        else:
            print(0)
    elif order[0] == "2":
        if order[1] in dic:
            dic[order[1]] = 0
    elif order[0] == "3":
        L = bisect_left(l,order[1])
        R = bisect(l,order[2])
        for i in range(L,R):
            if dic[l[i]]:
                print(l[i],dic[l[i]])