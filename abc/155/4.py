def faa(n,m):
    tmp = 0
    a = n + m
    if n == 9:
        tmp = 1
    else:
        tmp = n+1
    b = tmp + m + 1
    c = tmp + (10-m)

    return min(a,b,c) 

N = input()
if len(N) == 1:
    a = int(N)
    b = 10 - int(N)
    print(min(a,b))
    exit()
ans = 0
for i in range(len(N)-1):
    f = int(N[i])
    ff = int(N[i+1])
    ans += faa(f,ff)
print(ans)


