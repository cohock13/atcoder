dic = {}

for i in range(int(input())):
    order = list(input().split())

    if order[0] == "0":
        if order[1] in dic:
            dic[order[1]] = int(order[2])
        else:
            dic[order[1]] = int(order[2])
    elif order[0] == "1":
        if order[1] in dic:
            print(dic[order[1]])
        else:
            print(0)
    elif order[0] == "2":
        if order[1] in dic:
            dic.pop(order[1])
