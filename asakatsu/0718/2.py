n = list(map(int,input().split()))

s = sum([i%2 for i in n])

if s == 0 or s == 3:
    m = max(n)
    res = 0
    for i in n:
        res += (m-i)//2
    print(res)
elif s == 1:
    for i in range(3):
        if n[i]%2 == 0:
            n[i] += 1
    res = 1
    m = max(n)
    for i in n:
        res += (m-i)//2
    print(res)
else:##s == 2
    for i in range(3):
        if n[i]%2:
            n[i] += 1
    res = 1
    m = max(n)
    for i in n:
        res += (m-i)//2
    print(res)

