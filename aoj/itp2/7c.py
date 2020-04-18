import bisect

S = []
l = 0
for i in range(int(input())):
    order = tuple(map(int,input().split()))
    value = order[1]
    x = bisect.bisect_left(S,value)

    if order[0] == 0:
        if l:
            if 0 <= x < l:
                if S[x] != value:
                    S.insert(x,value)
                    l += 1
            else:
                S.append(value)
                l += 1
        else:
            S.append(value)
            l += 1
        print(l)
    elif order[0] == 1:

        if 0 <= x < l:
            if S[x] == value:
                print(1)
            else:
                print(0)
        else:
            print(0)
    elif order[0] == 2:
        if 0 <= x < l:
            if S[x] == value:
                S.remove(value)
                l -= 1
    else:
        left = bisect.bisect_left(S,order[1])
        right = bisect.bisect(S,order[2])
        for i in range(left,right):
            print(S[i])

