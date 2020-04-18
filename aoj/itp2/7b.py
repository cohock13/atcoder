S = set()

for i in range(int(input())):
    order,value = map(int,input().split())

    if order == 0:
        S.add(value)
        print(len(S))
    elif order == 1:
        print(1 if value in S else 0)
    else:
        S.discard(value)