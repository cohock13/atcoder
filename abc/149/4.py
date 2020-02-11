N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

win = {"r":P,"s":R,"p":S}
tmp = [1]*N
ans = 0

for i in range(N):
    if i<K:
        ans += win[T[i]]
        tmp[i] = 0
    else:
        if T[i]!=T[i-K] or tmp[i-K]:
            ans += win[T[i]]
            tmp[i] = 0

print(ans)



