from collections import Counter

N,K = map(int,input().split())
A = list(map(int,input().split()))

C = Counter(A).most_common()

ans = 0
for i in range(len(C)):
    if i >= K:
        ans += C[i][1]

print(ans)