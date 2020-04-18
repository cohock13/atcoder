S = set()

for _ in range(int(input())):
    order = tuple(map(int,input().split()))
    value = order[1]

    if order[0] == 0:
        S.add(value)
        print(len(S))
    elif order[0] == 1:
        if value in S:
            print(1)
        else:
            print(0)
    elif order[0] == 2:
        S.discard(value)
    else:
        if len(S) > order[2] - order[1]:
            for i in range(order[1],order[2]+1):
                if i in S:
                    print(i)
        else:
            tmp = sorted(S)
            for i in tmp:
                if order[1] <= i <= order[2]:
                    print(i)