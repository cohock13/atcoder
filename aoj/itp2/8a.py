dic = {}

for i in range(int(input())):
    order = list(input().split())

    if order[0] == "0":
        if order[1] in dic:
            dic[order[1]] = int(order[2])
        else:
            dic[order[1]] = int(order[2])
    else:
        print(dic[order[1]])