import bisect
import sys
def input():
    return sys.stdin.readline().strip()
S = []
count = {}
total = 0

for _ in range(int(input())):
    order = tuple(map(int,input().split()))
    value = order[1]
    if order[0] == 0:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
            bisect.insort(S,value)
        total += 1
        print(total)
    elif order[0] == 1:
        if value in count:
            print(count[value])
        else:
            print(0)
    elif order[0] == 2:
        if value in count:
            total -= count[value]
            count[value] = 0

    else:
        left = bisect.bisect_left(S,order[1])
        right = bisect.bisect(S,order[2])

        out = []

        for i in range(left,right):
            out += [S[i]]*count[S[i]]
        
        for i in out:
            print(i)
"""  
    print(S)
    print(count)
"""