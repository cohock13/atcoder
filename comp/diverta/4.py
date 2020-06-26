def factor(N):
    res = []
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            res.append(i)
            res.append(N//i)
    return sorted(list(set(res)))

N = int(input())
f = factor(N)
f.pop(0)

ans = 0
for n in f:
    tmp = n-1
    if N//tmp == N%tmp:
        ans += tmp
        
print(ans)
