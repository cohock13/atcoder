K = int(input())

ans = 1e9
for i in range(1,650000):
    ans = min(ans,sum(list(map(int,str(K*i)))))
print(ans)