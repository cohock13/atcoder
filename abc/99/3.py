def cash(a,N):
    ans = 0
    for i in reversed(range(len(a))):
        num = N//a[i]
        N -= a[i]*num
        ans += num
    return ans


N = int(input())

cash6 = []
cash9 = []
for i in range(1000):
    tmp = 6**i
    if tmp>N:
        break
    cash6.append(tmp)
for j in range(1000):
    tmp = 9**j
    if tmp>N:
        break
    cash9.append(tmp)

ans = 1e9
for i in range(N+1):
    ans = min(ans,cash(cash6,i)+cash(cash9,N-i))
print(ans)