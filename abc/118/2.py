N,M = map(int,input().split())

a = [0]*31

for i in range(N):
    questionary = list(map(int,input().split()))
    for i in range(1,questionary[0]+1):
        a[questionary[i]] += 1

ans = 0

for i in a:
    if i == N:
        ans += 1

print(ans)