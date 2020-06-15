cnt = [0]*(10**6+1)
conv = [0]*(10**6+1)

N = int(input())
A = list(map(int,input().split()))

for i in A:
    cnt[i] += 1

ans = 0##割り切れないものの数
for i in range(1,10**6+1):
    if cnt[i] == 1 and conv[i] == 0:##配列に1回のみ出現&&他の倍数でない
        ans += 1 
    if conv[i] == 1 or cnt[i] == 0:
        continue
    for j in range(10**6//i+1):##その数の倍数をメモ
        conv[i*j] = 1

print(ans)
