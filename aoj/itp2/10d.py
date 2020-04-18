
mask = []
for i in range(int(input())):
    tmp = list(map(int,input().split()))
    s = 0
    for j in tmp[1:]:
        s += 2**j
    mask.append(s)


b = 0
for i in range(int(input())):
    q,m = map(int,input().split())

    if q == 0:##test
        print((b>>m)&1)
    elif q == 1:##set
        b = b|mask[m]
    elif q == 2:##clear
        b = b & ~mask[m]
    elif q == 3:##flip
        b = b^mask[m]
    elif q == 4:##all
        print(1 if b&mask[m]==mask[m] else 0)
    elif q == 5:##any
        print(1 if b&mask[m] else 0)
    elif q == 6:##none
        print(1 if not b&mask[m] else 0)
    elif q == 7:##count
        print((format(b&mask[m],"032b")).count("1"))
    elif q == 8:##val
        print(b&mask[m])


