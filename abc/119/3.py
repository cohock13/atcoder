def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

def f(a,A):
    if len(a) == 0:
        return 1e12
    return (len(a)-1)*10 + abs(sum(a)-A)

N,A,B,C = map(int,input().split())
l = [int(input()) for i in range(N)]

ans = 1e12
for i in range(4**N+1):
    tmp = list(base_10_to_n(i,4).zfill(N))
    a,b,c = [],[],[]
    for s,t in zip(tmp,l):
        if s == "1":
            a.append(t)
        elif s == "2":
            b.append(t)
        elif s == "3":
            c.append(t)
    ans = min(ans,f(a,A)+f(b,B)+f(c,C))

print(ans)
        
        
