N = int(input())
S = input()

s = "b"
res = ["b"]
for i in range(101):
    if i%3 == 0:
        s = "a"+s+"c"
    elif i%3 == 1:
        s = "c"+s+"a"
    else:
        s = "b"+s+"b"
    res.append(s)

if S in res:
    print(res.index(S))
else:
    print(-1)