N = int(input())
K = list(map(int,input().split()))

ans = [K[0]]

for i in range(N-2):
    ans.append(min(K[i],K[i+1]))

ans.append(K[-1])

print(*ans)