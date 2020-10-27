S = input()
T = input()

ls = len(S)
lt = len(T)


ans = 1e10

for i in range(ls-lt+1):
    tmp = S[i:i+lt]
    cnt = 0
    for j in range(lt):
        if tmp[j] != T[j]:
            cnt += 1
    ans = min(ans,cnt)

print(ans)