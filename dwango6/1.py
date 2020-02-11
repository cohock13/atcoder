N = int(input())

s = []

for i in range(N):
    s.append(list(input().split()))
    
X = input()

ans = 0

for i in range(N):
    if s[i][0] == X:
        for i in range(i+1,N):
            ans += int(s[i][1])
        break

print(ans)

    