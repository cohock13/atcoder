from bisect import bisect,bisect_left,insort
dic = {}
l = []
for i in range(int(input())):
    order = list(input().split())

    if order[0] == "0":
        if not order[1] in dic:
            dic[order[1]] = []
            insort(l,order[1])
        dic[order[1]].append(int(order[2]))
    elif order[0] == "1":
        if order[1] in dic:
            for i in dic[order[1]]:
                print(i)
    elif order[0] == "2":
        if order[1] in dic:
            dic[order[1]] = []

    elif order[0] == "3":
        L = bisect_left(l,order[1])
        R = bisect(l,order[2])
        for i in range(L,R):
            for j in dic[l[i]]:
                print(l[i],j)
