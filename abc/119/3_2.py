def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

def f(a,la,A):
    if la == 0:
        return 1e12
    return (la-1)*10 + abs(a-A)

N,A,B,C = map(int,input().split())
l = [int(input()) for i in range(N)]

ans = 1e12
for i in range(4**N+1):
    tmp = list(base_10_to_n(i,4).zfill(N))
    a,la,b,lb,c,lc = 0,0,0,0,0,0
    for s,t in zip(tmp,l):
        if s == "1":
            a += t
            la += 1
        elif s == "2":
            b += t
            lb += 1
        elif s == "3":
            c += t
            lc += 1
    ans = min(ans,f(a,la,A)+f(b,lb,B)+f(c,lc,C))

print(ans)
        