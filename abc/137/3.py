N = int(input())
S = []
for i in range(N):
    S.append(input())

dic = {}
ans = 0

for i in S:
    tmp = "".join(sorted(i))
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
    
for i in dic.values():
    ##sum 1 to i-1 = (i^2-i)/2
    ans += (i*(i-1))//2

print(ans)





