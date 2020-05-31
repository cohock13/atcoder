K,S = map(int,input().split())


ans = 0

for i in range(K+1):
    for j in range(K+1):
        z = S - i - j
        if 0 <= z <= K:
            ans += 1

print(ans)