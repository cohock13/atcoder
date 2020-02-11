N = int(input())
H = list(map(int,input().split()))

ans = 0
i = 0

for k in range(N):
    tmp = 0
    while i<N-1:
        if H[i]>=H[i+1]:
            tmp += 1
            i += 1
        else:
            break
    ans = max(tmp,ans)
    if i >= N-1:
        break
    i += 1
    
    
print(ans)
