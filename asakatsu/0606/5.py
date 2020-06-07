n = int(input())
a = list(map(int,input().split()))


def check_1(a):
    
    ##正負正...
    res = 0
    s = 0
    for i in range(n):
        s += a[i]
        if i%2 == 0:
            if s <= 0:
                res += abs(s) + 1
                s = 1
        else:
            if s >= 0:
                res += abs(s) + 1
                s = -1
    return res

def check_2(a):
    ##負正負...
    res = 0
    s = 0
    for i in range(n):
        s += a[i]
        if i%2 == 0:
            if s >= 0:
                res += abs(s)+ 1
                s = -1
        else:
            if s <= 0:
                res += abs(s) + 1 
                s = 1
    return res

b = a[:]
print(min(check_1(a),check_2(b)))
